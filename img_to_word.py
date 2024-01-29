import re
import string
from PIL import Image
import pytesseract
from docx import Document
from unidecode import unidecode

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def sanitize_text(text):
    sanitized_text = re.sub(r'[^\x20-\x7E]', '', text)
    return sanitized_text

def save_text_to_word(text, output_path):
    doc = Document()
    sanitized_text = sanitize_text(text)
    doc.add_paragraph(sanitized_text)
    doc.save(output_path)

image_path = 'assets/invoice-sample.jpg'

result_text = extract_text_from_image(image_path)

output_word_path = 'assets/word_output_files/sample.docs'

save_text_to_word(result_text, output_word_path)

print(f"Text extracted from image and saved to {output_word_path}")
