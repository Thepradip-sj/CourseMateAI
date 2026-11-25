import os
from dotenv import load_dotenv

load_dotenv()

# API KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini Models
EMBEDDING_MODEL = "gemini-embedding-001"

LLM_MODEL = "gemini-2.5-flash"

# Chunk Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval Configuration
RETRIEVER_K = 4
FETCH_K = 10

# Directories
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

UPLOAD_DIR = os.path.join(BASE_DIR, "data", "uploads")

CHROMA_DIR = os.path.join(BASE_DIR, "data", "chroma_db")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_DIR, exist_ok=True)