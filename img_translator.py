from PIL import Image
from googletrans import Translator
import pytesseract

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

def main(image_path, target_language='en'):
    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print(f"Extracted Text: {extracted_text}")

        translated_text = translate_text(extracted_text, target_language)

        print(f"Translated Text ({target_language}): {translated_text}")
    else:
        print("No text found in the image.")

if __name__ == "__main__":
    example_image_path = 'assets/invoice-sample.jpg'
    

    target_language = 'fr'

    main(example_image_path, target_language)
