from backend.ingestion.pdf_loader import extract_text_from_pdf
from backend.ingestion.chunker import chunk_text
from backend.llm.generator import generate_answer
from backend.retrieval.vector_store import create_vector_store
from backend.retrieval.retriever import retrieve_chunks

text = extract_text_from_pdf("sample_pdfs/sample.pdf")

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

# Generate final answer
answer = generate_answer(query, results)

print("\nFinal Answer:\n")
print(answer)