import numpy as np
import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time

#loading and resizing
image = cv2.imread('car.jpeg')
image = imutils.resize(image, width=500)
cv2.imshow("Original Image", image)


#preprocessing the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1 - Grayscale Conversion", gray)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 170, 200)


#Finding contours and identifying the number plate region
cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCnt = None

count = 0
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        NumberPlateCnt = approx
        break

# Masking the part other than the number plate
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
new_image = cv2.bitwise_and(image, image, mask=mask)
cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
cv2.imshow("Final_image", new_image)

# Configuring Tesseract OCR and extracting text from the number plate region
config = ('-l eng --oem 1 --psm 3')
text = pytesseract.image_to_string(new_image, config=config)

# Storing the extracted data in a CSV file
raw_data = {'date': [time.asctime(time.localtime(time.time()))],
            'v_number': [text]}

df = pd.DataFrame(raw_data, columns=['date', 'v_number'])
df.to_csv('data.csv')

# Print recognized text
print(text)

cv2.waitKey(0)
