from pdf2docx import parse
from pdf2docx import Converter
from PIL import Image
import fitz
import pytesseract
from docx import Document
import io
import re

def pdf_to_word(pdf_path, output_word_path):
    doc = Document()

    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text = page.get_text()
        doc.add_paragraph(text)

    pdf_document.close()

    doc.save(output_word_path)
    
pdf_path = 'assets/student.pdf'
output_word_path = 'assets/word_output_files/sample2.docs'


pdf_to_word(pdf_path, output_word_path)

print(f"Text extracted from image and appended to the Word document: {output_word_path}")
