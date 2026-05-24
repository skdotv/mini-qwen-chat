from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_PATH = BASE_DIR / "documents" / "NIPS-2017-attention-is-all-you-need-Paper.pdf"
DB_PATH= BASE_DIR / "chroma_db"

PDF_FILES_PATH = Path(BASE_DIR / "documents").glob("*.pdf")

documents = []

for pdf in PDF_FILES_PATH:
    print(f"Loading {pdf.name}...")
    loader = PyPDFLoader(str(pdf))
    docs = loader.load()
    documents.extend(docs)
    

# #Load PDF 
# loader = PyPDFLoader(str(PDF_PATH))
# docs = loader.load()

# split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

#Embeding model
embeddings=OllamaEmbeddings(model="nomic-embed-text")

#Create Vector DB
vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=str(DB_PATH))


print("RAG database created successfully")
