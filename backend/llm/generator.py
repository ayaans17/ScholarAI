import os
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

def generate_answer(query, retrieved_docs):

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
    You are an academic research assistant.

    Answer the question ONLY using the provided context.

    If the answer is not in the context, say:
    "I could not find relevant information in the document."

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content