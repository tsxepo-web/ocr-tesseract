import fitz  # PyMuPDF

pdf_path = 'assets/student.pdf'



def pdf_to_text(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text += page.get_text()

    pdf_document.close()
    return text

pdf_text = pdf_to_text(pdf_path)

print(pdf_text)
