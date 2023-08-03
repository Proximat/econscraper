import os
import PdfReader
import re

def extract_pdf_metadata_and_title_info(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader.PdfFileReader(file)
        info = pdf_reader.getDocumentInfo()

        # Extract metadata
        filename = file_path.split("/")[-1]
        author = info.author.strip() if info.author else None
        title = info.title.strip() if info.title else None
        year_published = None

        # Extract year from metadata
        if info.get('/CreationDate'):
            year_published = info['/CreationDate'][2:6]

        # If no year found in metadata, try to extract from the title or filename
        if not year_published:
            year_published = extract_year_from_title(filename) or extract_year_from_title(title)

        return filename, author, title, year_published

def extract_year_from_title(title):
    # Try to extract the year from the title using regular expression
    # Adjust the regex pattern based on how your titles are structured
    pattern = r'\b(19|20)\d{2}\b'
    match = re.search(pattern, title)
    if match:
        return match.group()

def process_pdfs_in_folder(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Filter only PDF files
    pdf_files = [file for file in file_list if file.lower().endswith(".pdf")]

    # Iterate through each PDF file and extract metadata and title info
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        filename, author, title, year_published = extract_pdf_metadata_and_title_info(pdf_path)

        # Do something with the extracted information (e.g., print or save to a file)
        print("File:", filename)
        print("Author:", author)
        print("Title:", title)
        print("Year Published:", year_published)
        print("---")

# Example usage:
folder_path = "downloads"
process_pdfs_in_folder(folder_path)
