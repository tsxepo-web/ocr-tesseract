from docx import Document

def save_text_to_word(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

example_text = "This is an example text. Hello, World!"

output_word_path = 'assets/word_output_files/sample3.docs'

save_text_to_word(example_text, output_word_path)

print(f"Text saved to Word document: {output_word_path}")
