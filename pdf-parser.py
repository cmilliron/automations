import os
from PyPDF2 import PdfReader


def parse_pdf_to_text(pdf_path):
    """
    Parses a PDF file and extracts its text using PyPDF2.
    """
    text = ""
    try:
        reader = PdfReader(pdf_path)
        # Iterate through all the pages and extract text
        for page_num, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text += f"--- Page {page_num} ---\n" + page_text + "\n\n"
            else:
                text += f"--- Page {page_num} ---\n*No text found on this page.*\n\n"
    except Exception as e:
        # Log any error encountered during parsing.
        text = f"*Error reading {pdf_path}: {e}*\n"
    return text


def create_markdown_from_pdfs(pdf_folder, output_md):
    """
    Walks through the given folder, extracts text from all PDF files,
    and writes the information into a formatted markdown file.
    """
    markdown_content = "# PDF Extraction Results\n\n"

    # Loop through all files in the given folder
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"Processing {filename} ...")
            pdf_text = parse_pdf_to_text(pdf_path)

            # Append PDF title as a markdown header
            markdown_content += f"## {filename}\n\n"
            markdown_content += pdf_text + "\n"

    # Write the aggregated markdown content to the output file
    with open(output_md, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)
    print(f"Markdown file successfully written to {output_md}")


if __name__ == "__main__":
    # Specify the directory containing your PDFs
    pdf_directory = "/Users/codymilliron/Library/CloudStorage/GoogleDrive-cody@millironconsulting.com/My Drive/For AI Rundown"  # Update this path accordingly
    # Define the output markdown file name/path
    output_markdown = "/Users/codymilliron/Downloads/output.md"

    create_markdown_from_pdfs(pdf_directory, output_markdown)