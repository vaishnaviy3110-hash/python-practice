import chromadb
from sentence_transformers import SentenceTransformer

from document_processor import load_documents, chunk_text
from config import EMBEDDING_MODEL, CHROMA_DB_PATH


# Load the embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Create a local ChromaDB client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# Create or get the knowledge base collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)

# Load documents
documents = load_documents()

# Store chunks and embeddings
chunk_id = 0

for document in documents:
    chunks = chunk_text(document["content"])

    for chunk in chunks:

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(chunk_id)],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[
                {
                    "filename": document["filename"]
                }
            ]
        )

        chunk_id += 1


print("Vector database created successfully!")
print("Number of stored chunks:", collection.count())