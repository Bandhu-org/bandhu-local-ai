import os
from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "bandhu_ai")

# Init
chroma_client = Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_PATH))
collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_context(query, k=3):
    embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=k)
    documents = results.get("documents", [[]])[0]
    sources = results.get("metadatas", [[]])[0]
    
    # Format
    context = "\n\n".join([f"> {doc}" for doc in documents])
    return context, sources
