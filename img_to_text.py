import cv2 as cv
import pytesseract
import numpy as np

from img_preprocess import get_grayscale, thresholding, opening, canny

img = cv.imread('assets/invoice-sample.jpg')

gray = get_grayscale(img)
threshold = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(threshold, config=custom_config)

print(text)