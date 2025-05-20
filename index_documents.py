import os
from pathlib import Path
from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Config
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "bandhu_ai")
DOCS_PATH = "./docs"

# Init
chroma_client = Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=CHROMA_PATH))
collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Indexing
def read_documents(path):
    for file in Path(path).glob("*.md"):
        with open(file, "r", encoding="utf-8") as f:
            yield file.name, f.read()

def chunk(text, size=500, overlap=50):
    words = text.split()
    for i in range(0, len(words), size - overlap):
        yield " ".join(words[i:i + size])

# Index loop
for filename, content in read_documents(DOCS_PATH):
    for i, chunk_text in enumerate(chunk(content)):
        uid = f"{filename}-{i}"
        collection.add(
            documents=[chunk_text],
            metadatas=[{"source": filename}],
            ids=[uid]
        )
print("Indexation terminée.")
