import pyautogui
import cv2
import pytesseract
import numpy as np
import math
from scipy import ndimage

def ocr(imageLoc):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img = cv2.imread(imageLoc)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    gray = cv2.bitwise_not(img_bin)
    kernel = np.ones((2, 1), np.uint8)

    img = cv2.erode(gray, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)
    out_below = pytesseract.image_to_string(img)
    return out_below.strip()

def clubCleaner(club):
   return {
        '5wwwood': '5 wood',
        '3wood': '3 wood'
    }.get(club, club)

# determine rotation of image

def main():

    clubImageName = 'club.png'
    clubIMG = pyautogui.screenshot(region=(1170, 115, 120, 20), imageFilename=clubImageName)
    club = clubCleaner(ocr(clubImageName).lower())
    windspeedImageName = "windspeed.png"
    windspeedIMG = pyautogui.screenshot(region=(590, 45, 70, 20), imageFilename=windspeedImageName)
    windspeed = ocr(windspeedImageName).lower()
    print("Club:", club)
    print("Wind", windspeed)
if __name__=="__main__":
    main()