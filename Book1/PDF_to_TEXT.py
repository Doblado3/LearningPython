# a basic example of reading data from a .pdf file with Python, using `pdf2image` to convert it to images, and then using the
# openCV and `tesseract` libraries to extract the text


#To-Do task: separate the process of converting pdf-to-image and image-to-text in two diferrent scripts and 
#make them to work without writing any line of code.

import os
from pdf2image import convert_from_path
import glob # Another built-in library
import cv2 #openCV library for python
import pytesseract #tesseract python library version

# Set up paths and file names
pdf_name = "SafetyNet"
pdf_source_file = os.path.join("data", f"{pdf_name}.pdf")
tesseract_cmd_path = "C:/Users/Pablo/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

# Ensure the target folder exists
if not os.path.isdir(pdf_name):
    os.mkdir(pdf_name)

# Convert PDF to images
pages = convert_from_path(pdf_source_file, 300)

# Save each page as an image
for page_num, page in enumerate(pages):
    filename = os.path.join(pdf_name, f"p{page_num}.png")
    page.save(filename, 'PNG')

# Process each image and extract text
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path  # Set Tesseract executable path
for img_file in glob.glob(os.path.join(pdf_name, '*.png')):
    text_filename = os.path.splitext(os.path.basename(img_file))[0]  # Get the base name without extension

    # Create and open the output text file
    output_file_path = os.path.join(pdf_name, f"{text_filename}.txt")
    with open(output_file_path, "w") as output_file:
        # Read the image
        img = cv2.imread(img_file)
        if img is None:
            print(f"Error reading image file {img_file}")
            continue

        # Extract text from the image
        converted_text = pytesseract.image_to_string(img)

        # Write the extracted text to the file
        output_file.write(converted_text)
