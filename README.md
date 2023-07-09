# license-plate-recognition

In this code, the main objective is to extract the text from a car number plate image and store it in a CSV file. Here is a summary of the code.
Loading and resizing the image: I used the OpenCV library to read the image and resized it to a width of 500 pixels for better processing.

Preprocessing the image: I converted the image to grayscale and applied bilateral filtering to reduce noise. Then, I performed edge detection using the Canny algorithm to identify the edges of objects in the image.

Finding contours and identifying the number plate region: I found contours in the edge-detected image and sorted them based on their area. The contour with four vertices (a quadrilateral shape) is considered as the number plate region.

Masking the number plate region: I created a binary mask with the same shape as the grayscale image and drew the identified number plate contour on it. This masked out the region of interest, i.e., the number plate, while keeping the rest of the image black.

Extracting text using Tesseract OCR: I configured the Tesseract OCR (Optical Character Recognition) engine to recognize English language text and set the page segmentation mode. Then, I applied the OCR on the masked number plate region to extract the text.

Storing the extracted data: I created a DataFrame using the Pandas library to store the extracted text and the current date. Finally, I saved this data in a CSV file named 'data.csv'.

Displaying and printing the recognized text: I displayed the final processed image with the number plate region highlighted, and printed the extracted text.

This project demonstrates my skills in image processing, contour detection, OCR, and data handling using Python libraries such as OpenCV, pytesseract, and Pandas.
