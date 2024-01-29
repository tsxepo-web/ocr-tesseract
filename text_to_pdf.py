from reportlab.pdfgen import canvas

def save_text_to_pdf(text, output_path):
    pdf_canvas = canvas.Canvas(output_path)
    
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(100, 700, text)

    pdf_canvas.save()


example_text = "This is an example text. Hello, World!"

output_pdf_path = 'assets/word_output_files/sample3.pdf'

save_text_to_pdf(example_text, output_pdf_path)

print(f"Text saved to PDF document: {output_pdf_path}")
