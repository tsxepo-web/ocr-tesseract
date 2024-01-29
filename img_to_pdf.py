from reportlab.pdfgen import canvas
from PIL import Image

def save_image_to_pdf(image_path, output_path):
    img = Image.open(image_path)
    pdf_canvas = canvas.Canvas(output_path, pagesize=img.size)
    pdf_canvas.drawInlineImage(image_path, 0, 0)
    pdf_canvas.save()


example_image_path = 'assets/characters.jpg'

output_pdf_path = 'assets/word_output_files/sample4.pdf'

save_image_to_pdf(example_image_path, output_pdf_path)

print(f"Image saved to PDF document: {output_pdf_path}")
