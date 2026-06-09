#from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_text(pages):
    print("Pages received:", len(pages))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for page in pages:

        split_texts = splitter.split_text(page["text"])

        for text in split_texts:
            chunks.append({
                "text": text,
                "page": page["page"],
                "source": page["source"]
            })

    return chunks