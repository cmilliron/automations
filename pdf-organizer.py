import os
import re
from PyPDF2 import PdfReader

# Set the directory containing the PDF files
directory = '/Users/codymilliron/Downloads/pdf-test'

# Define a regular expression to match one or more digits
number_pattern = re.compile(r"s u p p o r t @ e t s y c h e c k \. c o m")

# Loop over each file in the directory
for filename in os.listdir(directory):
    # Process only PDF files (ignoring case)
    if filename.lower().endswith('.pdf'):
        file_path = os.path.join(directory, filename)
        try:
            # Create a PdfReader object to extract text from the PDF
            reader = PdfReader(file_path)
            text = ""

            # Loop through each page in the PDF and extract text
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            print(text)
            # Search for the first occurrence of a number in the extracted text
            match = number_pattern.search(text)
            if match:
                number_found = match.group()

                # Create a new file name (e.g., prepend the found number)
                new_filename = f"test completed"
                new_file_path = os.path.join(directory, new_filename)

                # Print the renaming action and perform the renaming
                print(f"Renaming '{filename}' to '{new_filename}'")
                os.rename(file_path, new_file_path)
            else:
                print(f"No number found in '{filename}'.")
        except Exception as e:
            print(f"Error processing '{filename}': {e}")