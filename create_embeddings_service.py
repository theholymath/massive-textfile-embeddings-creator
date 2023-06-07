# Purpose: Create a service that creates embeddings for a given text
# assumes all text files with extension *.txt in directory `data/`

from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings, SentenceTransformerEmbeddings

loader = DirectoryLoader('data/', glob="./*.txt", loader_cls=TextLoader)
documents = loader.load()

#splitting the text into
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

## normal HF embeddings
model_name = "sentence-transformers/all-mpnet-base-v2"
hf = HuggingFaceEmbeddings(model_name=model_name)

vectordb = Chroma.from_documents(documents=texts, 
                                 embedding=hf,
                                 persist_directory=persist_directory)

# persiste the db to disk
print("Writing Vector DB to disk")
vectordb.persist()
vectordb = None
