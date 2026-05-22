def retrieve_chunks(query, vector_store, k=3):

    docs = vector_store.similarity_search(
        query,
        k=k
    )

    return docs