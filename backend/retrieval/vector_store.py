from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):
    texts = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "page": chunk["page"],
            "source": chunk["source"]
        }
        for chunk in chunks
    ]

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    return vector_store