from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding='UTF8') as f:
        f.read()


setup(
  name='faiss-minio-connection',
  version='0.0.2',
  author='ilya_a',
  author_email='iakulpypi@mail.ru',
  description='Combining FAISS work with S3 cloud storage.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Ilya-Akulov/FAISS-Minio',
  packages=find_packages(),
  install_requires=['boto3',
                    'fastapi==0.89.1',
                    'faiss-cpu==1.8.0',
                    'langchain==0.2.0',
                    'langchain-community==0.2.0',
                    'langchain-core==0.2.1',
                    'pydantic==1.10.15',
                    'numpy==1.26.4',
                    ],
  classifiers=[
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='FAISS Minio',
  project_urls={
    'GitHub': 'https://github.com/Ilya-Akulov/FAISS-Minio'
  },
  python_requires='>=3.9.13'
)