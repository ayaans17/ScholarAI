from backend.ingestion.pdf_loader import extract_text_from_pdf
from backend.ingestion.chunker import chunk_text
from backend.llm.generator import generate_answer
from backend.retrieval.vector_store import create_vector_store
from backend.retrieval.retriever import retrieve_chunks

text = extract_text_from_pdf("sample_pdfs/sample.pdf")
print("Pages extracted:", len(text))

print(text[0])
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")

vector_store = create_vector_store(chunks)

print("Vector store created successfully!")

query = "What challenges in text feature extraction does the paper address?"

# Retrieve chunks
results = retrieve_chunks(query, vector_store)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(results):
    print(f"\nChunk {i+1}:\n")
    print(doc.page_content[:300])
    print(doc.metadata)

# Generate final answer
answer = generate_answer(query, results)

print("\nFinal Answer:\n")
print(answer)

sources = set()

for doc in results:
    sources.add(
        (
            doc.metadata["source"],
            doc.metadata["page"]
        )
    )

print("\nSources:")

for source, page in sorted(sources):
    print(f"{source} (Page {page})")