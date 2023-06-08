# massive-textfile-embeddings-creator

This repository contains code for an end-to-end documnets --> vector database indexing --> converstaional LLM.

There are three major processes:
1. Creating a vector database,
1. Querying the DB,
1. Querying the DB and using a LLM to understand and syntehsize the data into a conversational format.

The key technologies used are:
1. [ChromaDB](https://www.trychroma.com/) (python bindings) is an open-source vector index. 
1. [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers) 
1. [Langchain](https://python.langchain.com/en/latest/) As a utility and pipeline tool mostly. 
1. [ChatGPT 3.5 Turbo]()

## Quick Start

To run the programs you must
* **clone the repo** 
    * `git clone https://github.com/theholymath/massive-textfile-embeddings-creator.git` 
* **Get the data**,
    * Data must be in the data directory (`mkdir` if it does not exist). 
* **Create the index** (whcih can be built from the data),
    * set up the `persistent directory` in the `create_embeddings_service.py` file. 
* **Python environemnt and updated pip**
    * Create a virtual environment: `python3 -m venv .env`
    * update pip to the latest (THIS IS CRITICAL OR YOUR PACKAGES WILL NOT INSTALL CORRECTLY)
    * Install requirements `pip install -r requirements.txt`



## Step 1: Creating a Vector Databse (Index)

This is done using the `create_embeddings_service.py`.

In this file you must decide
* which embeddings to use,
* which type of vector database or vector index to use (ChromaDB, Pinecone, FAISS),
* How to partition the chunking,
* How to preprocess the data to capture all the relevant information, i.e., how do you want to capture the metadata?

There must be files in a `data` directory. The python package has a suite of "loaders" that can load various types of documents: pdf, csv, txt, ect. The code is set up to glob txt files.

If the files are mixed I believe there is a `DirectoryLoader` that can handle multiple file types. 

## Step 2: Set up a Vector DB "retreiver" using `langchain`

This can be done using the `query_db_retreiver,py` file. 

NOTE: YOU MUST USE THE SAME EMBEDDINGS YOU USED TO CREATE THE DB.

A typical execution command is something like 

> `python query_db_retreiver.py "Are there any US presidents that broke the law?"`

## STEP 3: Put into a web app (`streamlit`)

Make sure streamlit and streamlit_chat are installed,
> `pip install streamlit streamlit_chat`

Then run the app,
> `streamlit run chat_supreme_court_opinions.py`

It should work out of the box as long as the directory is pointing to the correct DB. Also, you will need to paste in your OpenAI API Key for it to work. Otherwise it will keep telling you it doesn't have enoug context. 

