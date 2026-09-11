from pathlib import Path
from config import CHROMA_DB_PATH

DATA_PATH = Path("data/raw")
def clean_text(text):
    """
    Clean unnecessary whitespace from document text.
    """

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def load_documents():
    """
    Load all TXT documents from the knowledge base.
    """

    documents = []

    for file_path in DATA_PATH.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        cleaned_text = clean_text(text)

        documents.append({
            "filename": file_path.name,
            "content": cleaned_text
        })

    return documents


def chunk_text(text, chunk_size=500, chunk_overlap=50):
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end - chunk_overlap

    return chunks


documents = load_documents()

print(f"Number of documents: {len(documents)}")


for document in documents:

    chunks = chunk_text(document["content"])

    print("\n" + "=" * 60)
    print(f"File: {document['filename']}")
    print(f"Number of chunks: {len(chunks)}")
    print("=" * 60)

    for index, chunk in enumerate(chunks):
        print(f"\nChunk {index + 1}:")
        print(chunk)