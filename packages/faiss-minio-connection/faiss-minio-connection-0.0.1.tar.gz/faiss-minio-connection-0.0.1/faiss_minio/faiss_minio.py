import os
import json
import boto3
import fastapi
import numpy as np
from typing import List
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores.faiss import dependable_faiss_import


class FaissMinio:
    NAME_FOLDER_COLLECTIONS = 'db_collections'

    def __init__(self,
                 embedding_model: HuggingFaceInstructEmbeddings,
                 minio_host: str,
                 minio_port: str,
                 minio_bucket: str,
                 login_minio: str,
                 password_minio: str,
                 collection_name: str):
        self._MINIO_HOST = minio_host
        self._MINIO_PORT = minio_port
        self._MINIO_BUCKET = minio_bucket
        self._EMBEDDING_MODEL = embedding_model
        self._COLLECTION_NAME = collection_name
        self.check_collection_exist(login_minio=login_minio,
                                    password_minio=password_minio)
        self._s3 = boto3.resource('s3',
                                  endpoint_url=f'http://{minio_host}:{minio_port}',
                                  aws_access_key_id=login_minio,
                                  aws_secret_access_key=password_minio
                                  )

    def check_collection_exist(self,
                               login_minio: str,
                               password_minio: str):
        s3_cli = boto3.client('s3',
                              endpoint_url=f'http://{self._MINIO_HOST}:{self._MINIO_PORT}',
                              aws_access_key_id=login_minio,
                              aws_secret_access_key=password_minio)
        list_collections = s3_cli.list_objects(Bucket=self._MINIO_BUCKET, Prefix=self.NAME_FOLDER_COLLECTIONS)['Contents']
        list_collections = list(
            set([collection['Key'].split(f'{self.NAME_FOLDER_COLLECTIONS}/')[1].split('/')[0] for collection in
                 list_collections]))

        if self._COLLECTION_NAME in list_collections:
            raise NameError(
                f'Коллекция с именем: "{self._COLLECTION_NAME}" уже существует!\nA collection with name: "{self._COLLECTION_NAME}" already exists!')

    def _decorator_save_db(from_documents):
        def prepare_atribute(self, vector_db):
            faiss = dependable_faiss_import()
            docstore_db = json.dumps(fastapi.encoders.jsonable_encoder(vector_db.docstore._dict))
            index_to_docstore_id = json.dumps(vector_db.index_to_docstore_id)
            index_db = faiss.serialize_index(vector_db.index)
            index_db_binary = json.dumps(index_db.tolist())
            return {'docstore_db': docstore_db,
                    'index_to_docstore_id': index_to_docstore_id,
                    'index_db_binary': index_db_binary}

        def save_minio(self,
                       docs_chunk):
            vector_db = from_documents(self, docs_chunk)
            dict_atribute_to_minio = prepare_atribute(self, vector_db)
            for key, values in dict_atribute_to_minio.items():
                obj = self._s3.Object(self._MINIO_BUCKET,
                                      f"/{self.NAME_FOLDER_COLLECTIONS}/{self._COLLECTION_NAME}/{key}.json")
                json_values = values
                obj.put(Body=json_values)
            return vector_db

        return save_minio

    @_decorator_save_db
    def from_documents(self,
                       docs_chunk: List[Document]):
        vector_db = FAISS.from_documents(docs_chunk, self._EMBEDDING_MODEL)
        return vector_db

    def _prepare_docstore(self,
                          json_file: str):
        def create_documents(content: str,
                             metadata: dict,
                             ) -> Document:
            content = content.replace('\xa0', '')
            contents = '\n'.join(list(filter(lambda x: x != '', content.split('\n'))))
            document = Document(page_content=contents,
                                metadata=metadata
                                )
            return document

        docs_json_faiss = json.loads(json_file)
        docstore_from_dict = InMemoryDocstore()
        for key, values in docs_json_faiss.items():
            _dict_doc = {key: create_documents(content=values['page_content'],
                                               metadata=values['metadata'])}
            docstore_from_dict.add(_dict_doc)
        return docstore_from_dict

    def _prepare_index(self,
                       json_file: str):
        chunk = json.loads(json_file)
        faiss = dependable_faiss_import()
        index_from_minio = faiss.deserialize_index(np.array(chunk, dtype=np.uint8))
        return index_from_minio

    def _prepare_index_to_docstore_id(self,
                                      json_file: str):
        _index_to_docstore_id = json.loads(json_file)
        _index_to_docstore_id = {int(key): value for key, value in _index_to_docstore_id.items()}
        return _index_to_docstore_id

    def _prepare_faiss_params(self):
        dict_atr_faiss_func = {'docstore_db': self._prepare_docstore,
                               'index_to_docstore_id': self._prepare_index_to_docstore_id,
                               'index_db_binary': self._prepare_index}
        dict_atr_faiss_val = {'docstore_db': None,
                              'index_to_docstore_id': None,
                              'index_db_binary': None}

        for s3_object in self._s3.Bucket(self._MINIO_BUCKET).objects.filter(
                Prefix=f'{self.NAME_FOLDER_COLLECTIONS}/{self._COLLECTION_NAME}/'):
            path, filename = os.path.split(s3_object.key)
            obj = self._s3.Object(self._MINIO_BUCKET, f"{path}/{filename}")
            data = obj.get()['Body'].read()
            atr_name = filename.split('.')[0]
            dict_atr_faiss_val[atr_name] = dict_atr_faiss_func[atr_name](data)

        return dict_atr_faiss_val

    def _load_db(self):
        dict_atr_faiss_val = self._prepare_faiss_params()
        faiss = FAISS(embedding_function=self._EMBEDDING_MODEL,
                      index=dict_atr_faiss_val['index_db_binary'],
                      docstore=dict_atr_faiss_val['docstore_db'],
                      index_to_docstore_id=dict_atr_faiss_val['index_to_docstore_id'],
                      )
        return faiss

    def as_retriever(self,
                     search_type: str,
                     search_kwargs: dict):
        vector_db = self._load_db()
        retriever_main = vector_db.as_retriever(search_type=search_type, search_kwargs=search_kwargs)
        return retriever_main
