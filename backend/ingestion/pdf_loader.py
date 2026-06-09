import fitz
import os
def extract_text_from_pdf(folder_path):
    pages=[]
    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            pdf_path = os.path.join(folder_path, filename)

            doc = fitz.open(pdf_path)

            for page_num, page in enumerate(doc):
                pages.append({
                    "text": page.get_text(),
                    "page": page_num + 1,
                    "source": filename
                })

    return pages