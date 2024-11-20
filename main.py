import langchain
import pinecone
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.llms import huggingface_pipeline
import os

def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    document=file_loader.load()
    return document

doc=read_doc("documents/")
doc