import pytesseract
from PIL import Image, ImageOps
import traceback
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_file):
    try:
        preprocessed_image = preprocess_image(image_file)

        # Open the image using PIL (Python Imaging Library)
        # image = Image.open(preprocessed_image)

        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(preprocessed_image)

        return extracted_text
    except Exception as e:
        traceback.print_exc()
        return None
    
def preprocess_image(image_file):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_file)

        # Convert the image to grayscale
        grayscale_image = ImageOps.grayscale(image)
        
        # Apply thresholding to convert to black and white
        threshold_value = 128  # You can adjust this threshold as needed
        threshold_image = grayscale_image.point(lambda p: p > threshold_value and 255)
        clear_folder("./tempCache/")
        threshold_image.save("./tempCache/threshold_image.png")

        return threshold_image
    except Exception as e:
        raise e

def clear_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                clear_folder(file_path)  # Recursively clear subdirectories
                os.rmdir(file_path)  # Remove the empty subdirectory

        print(f"Folder '{folder_path}' cleared successfully.")
    except Exception as e:
        raise e