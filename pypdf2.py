import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def process_pdfs_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            text = extract_text_from_pdf(pdf_path)
            
            # Lakukan sesuatu dengan teks, misalnya, tampilkan atau simpan ke file lain
            print(f"File: {filename}\nText:\n{text}\n{'='*50}\n")

if __name__ == "__main__":
    # Gantilah path sesuai dengan direktori tempat PDF Anda disimpan
    pdf_directory = "/Documents/JurnalE-LearningSMAN1Parongpong/BundelSkripsi_Seprianto/pdf/files"
    
    process_pdfs_in_directory(pdf_directory)
