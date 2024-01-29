import io
import fitz
from PIL import Image
import pytesseract
import cv2
import numpy as np

def pdf_to_images(pdf_path):
    images = []
    pdf_document = fitz.open(pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        pixmap = page.get_pixmap()
        
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        
        processed_image = preprocess_image(np.array(image))

        images.append(processed_image)

    pdf_document.close()
    return images

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresholded = thresholding(gray)    
    return thresholded

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

pdf_path = 'assets/docs.pdf'
# pdf_path = 'assets/student.pdf'


pdf_images = pdf_to_images(pdf_path)
full_text = ""

for i, img in enumerate(pdf_images):
    text = pytesseract.image_to_string(img)
    full_text += f"Page {i + 1} Text:\n{text}\n"

print(full_text)
