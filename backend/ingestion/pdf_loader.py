import fitz

def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)
    print("Total pages in PDF:", len(doc))

    text = ""
    pages = []

    for page_num, page in enumerate(doc):
        print(f"Page {page_num + 1} text length:", len(page.get_text()))
        pages.append({
            "text": page.get_text(),
            "page": page_num + 1
        })

    return pages