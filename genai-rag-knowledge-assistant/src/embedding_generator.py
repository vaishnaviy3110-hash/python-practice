from sentence_transformers import SentenceTransformer
from document_processor import load_documents, chunk_text
from config import EMBEDDING_MODEL

# Load the embedding model
model = SentenceTransformer(EMBEDDING_MODEL)

# Load documents from the knowledge base
documents = load_documents()

# Create chunks from all documents
all_chunks = []

for document in documents:
    chunks = chunk_text(document["content"])

    for chunk in chunks:
        all_chunks.append({
            "filename": document["filename"],
            "content": chunk
        })

# Extract only the text from chunks
chunk_texts = [chunk["content"] for chunk in all_chunks]

# Generate embeddings
embeddings = model.encode(chunk_texts)

print("Number of documents:", len(documents))
print("Number of chunks:", len(all_chunks))
print("Embedding shape:", embeddings.shape)

print("\nFirst chunk:")
print(all_chunks[0]["content"])

print("\nFirst 10 embedding values:")
print(embeddings[0][:10])