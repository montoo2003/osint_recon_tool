import PyPDF2

def extract_pdf_metadata(file_path):
    with open(file_path, "rb") as pdf:
        reader = PyPDF2.PdfReader(pdf)
        metadata = reader.metadata
        return metadata
