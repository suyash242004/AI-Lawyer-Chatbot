# from langchain_community.document_loaders import PDFPlumberLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_ollama import OllamaEmbeddings
# from langchain_community.vectorstores import FAISS

# #Step 1: Upload & Load raw PDF(s)

# pdfs_directory = 'pdfs/'

# def upload_pdf(file):
#     with open(pdfs_directory + file.name, "wb") as f:
#         f.write(file.getbuffer())


# def load_pdf(file_path):
#     loader = PDFPlumberLoader(file_path)
#     documents = loader.load()
#     return documents


# file_path = 'universal_declaration_of_human_rights.pdf'
# documents = load_pdf(file_path)
# #print("PDF pages: ",len(documents))

# #Step 2: Create Chunks
# def create_chunks(documents): 
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size = 1000,
#         chunk_overlap = 200,
#         add_start_index = True
#     )
#     text_chunks = text_splitter.split_documents(documents)
#     return text_chunks

# text_chunks = create_chunks(documents)
# #print("Chunks count: ", len(text_chunks))


# #Step 3: Setup Embeddings Model (Use DeepSeek R1 with Ollama)
# ollama_model_name="deepseek-r1:1.5b"
# def get_embedding_model(ollama_model_name):
#     embeddings = OllamaEmbeddings(model=ollama_model_name)
#     return embeddings

# #Step 4: Index Documents **Store embeddings in FAISS (vector store)
# FAISS_DB_PATH="vectorstore/db_faiss"
# faiss_db=FAISS.from_documents(text_chunks, get_embedding_model(ollama_model_name))
# faiss_db.save_local(FAISS_DB_PATH)




import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Optional OpenAI import - only if you want OpenAI fallback
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings

pdfs_directory = 'pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

def create_chunks(documents): 
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

file_path = 'universal_declaration_of_human_rights.pdf'
documents = load_pdf(file_path)
text_chunks = create_chunks(documents)

# Use environment variable to switch embedding backend
USE_OLLAMA = os.getenv("USE_OLLAMA", "true").lower() == "true"

if USE_OLLAMA:
    ollama_model_name = "deepseek-r1:1.5b"
    def get_embedding_model():
        return OllamaEmbeddings(model=ollama_model_name)
else:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    def get_embedding_model():
        return OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

embeddings = get_embedding_model()

FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, embeddings)
faiss_db.save_local(FAISS_DB_PATH)
