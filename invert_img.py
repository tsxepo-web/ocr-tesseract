from PIL import Image
import numpy as np

def invert_image(image_path, output_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    inverted_img_array = 255 - img_array
    inverted_img = Image.fromarray(inverted_img_array)
    inverted_img.save(output_path)

example_image_path = 'assets/characters.jpg'
output_inverted_path = 'assets/word_output_files/inverted_image.jpg'

invert_image(example_image_path, output_inverted_path)

print(f"Inverted image saved to: {output_inverted_path}")
