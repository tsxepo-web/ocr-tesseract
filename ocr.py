import cv2 as cv
import pytesseract
import numpy as np

img = cv.imread('assets/invoice-sample.jpg')

def get_grayscale(image):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def thresholding(image):
    return cv.threshold(image,0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv.erode(image, kernel, iterations = 1)

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

def canny(image):
    return cv.Canny(image, 100, 200)

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv.minAreaRect(coords)[1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
    return rotated

def match_template(image, template):
    return cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)
    

gray = get_grayscale(img)
threshold = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(threshold, config=custom_config)

print(text)