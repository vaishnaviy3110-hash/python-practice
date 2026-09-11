import chromadb
from sentence_transformers import SentenceTransformer

from config import EMBEDDING_MODEL, CHROMA_DB_PATH


# Load the embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Connect to our local ChromaDB
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

# Get the existing knowledge base
collection = client.get_collection(
    name="knowledge_base"
)


# Keep asking questions
while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    # Exit the program
    if query.lower() == "exit":
        print("Goodbye!")
        break

    # Handle empty questions
    if not query.strip():
        print("Please enter a question.")
        continue

    # Convert the question into an embedding
    query_embedding = model.encode(query).tolist()

    # Search for relevant information
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    # Combine retrieved chunks into context
    context = "\n\n".join(
        results["documents"][0]
    )

    print("\n" + "=" * 50)
    print("QUESTION")
    print("=" * 50)
    print(query)

    print("\n" + "=" * 50)
    print("SOURCES")
    print("=" * 50)

    for i in range(len(results["documents"][0])):

        source = results["metadatas"][0][i]["filename"]
        distance = results["distances"][0][i]

        print(
            f"{i + 1}. {source} | "
            f"Distance: {distance:.4f}"
        )

    print("\n" + "=" * 50)
    print("RETRIEVED CONTEXT")
    print("=" * 50)

    print(context)

    # Create the RAG prompt
    prompt = f"""
You are a helpful AI assistant for an AI Engineering
knowledge base.

Follow these rules:

1. Answer the user's question using only the provided context.
2. Do not make up or assume information.
3. If the answer is not present in the context, clearly say:
   "I could not find the answer in the knowledge base."
4. Keep the answer clear and relevant to the question.

Context:
{context}

Question:
{query}

Answer:
"""