import chromadb
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL, CHROMA_DB_PATH


# Load the embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Connect to the local ChromaDB
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# Get the existing knowledge base
collection = client.get_collection(
    name="knowledge_base"
)


# Ask the user a question
query = input("Ask a question: ")

# Convert the question into an embedding
query_embedding = model.encode(query).tolist()

# Search the knowledge base
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3,
    include=[
        "documents",
        "metadatas",
        "distances"
    ]
)


print("\n" + "=" * 50)
print("SEARCH QUERY")
print("=" * 50)

print(query)


print("\n" + "=" * 50)
print("RELEVANT RESULTS")
print("=" * 50)


for i, document in enumerate(results["documents"][0]):

    source = results["metadatas"][0][i]["filename"]
    distance = results["distances"][0][i]

    print(f"\n--- Result {i + 1} ---")
    print("Source:", source)
    print("Distance:", round(distance, 4))
    print("Content:")
    print(document)