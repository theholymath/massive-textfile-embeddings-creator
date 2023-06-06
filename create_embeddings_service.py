# Purpose: Create a service that creates embeddings for a given text
import os

#os.environ["OPENAI_API_KEY"] = ""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

# local import
from utilities.embeddings import LocalHuggingFaceEmbeddings

loader = DirectoryLoader('data/case_files/', glob="./*.txt", loader_cls=TextLoader)
documents = loader.load()

#splitting the text into
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

## OpenAI Embeddings COST A LOT ... use HuggingFace
embedding = LocalHuggingFaceEmbeddings('multi-qa-mpnet-base-dot-v1')

vectordb = Chroma.from_documents(documents=texts, 
                                 embedding=embedding,
                                 persist_directory=persist_directory)

# persiste the db to disk
vectordb.persist()
vectordb = None
