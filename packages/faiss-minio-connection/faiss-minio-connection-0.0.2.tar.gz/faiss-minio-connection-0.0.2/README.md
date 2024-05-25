# FAISS Minio Connection #

## Что такое FAISS Minio Connection? ##
Модуль дает возможность сохранять/загружать коллекции векторной базы данных в S3 хранилище - Minio.

----------

## Quick Guide ##
### Инициализация класса ###
Для инициализации класса, необходимо передать параметры подключения к бакету Minio и embeding_model, 
котрая должна иметь тип HuggingFaceInstructEmbeddings:

    famin = FaissMinio(embedding_model=embedding_model, 
                       minio_host=HOST_MINI0,
                       minio_port=PORT_MINIO,
                       minio_bucket=BUCKET_NAME,
                       login_minio=LOGIN_MINIO,
                       password_minio=PASSWORD_MINIO,
                       collection_name=NAME_COLLECTION)
    
В модуле реализовано две функции:
 - .from_documents(docs_chunk:List\[Document\])
 - .as_retriever(search_type:str, search_kwargs:dict)

### Создание векторной базы из документов ###

    vector_db = famin.from_documents(docs_chunk=doc_chunks)
При выполненении функции происходит загрузка данных в Minio. 
По умолчанию создается, если ее нет, папка "db_collections" в ней будут хранится все коллекции созданные с помощью библиотеки.
В этой папке создается папка с названием коллекции "NAME_COLLECTION" и уже в ней будут хранится все данные в формате "json".

Пример расположения файлов в бакете: "test_bucket/db_collections/test_collection/"

Данные состоят из:
 - docstore_db.json 
 - index_db_binary.json
 - index_to_docstore_id.json

### Создание ретривера из векторной базы ###
    retriver = famin.as_retriever(search_type="",
                                  search_kwargs={})
При выполнении функции происходит загрузка данных коллекции, для которой создается ретривер.
Данные преобразовываются в необходимый вид для FAISS. 
Далее инициализируется база данных FAISS и выполняется ее встроенная функция .as_retriever:

    faiss = FAISS(embedding_function=EMBEDDING_MODEL,
                  index=index_db_binary,
                  docstore=docstore_db,
                  index_to_docstore_id=index_to_docstore_id,
                     )
