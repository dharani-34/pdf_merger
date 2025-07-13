import PyPDF2
import os

def merge_pdfs(pdf_list, output_name):
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_name)
    merger.close()
    print(f"✅ Merged file saved as '{output_name}'")

def get_pdf_files():
    files = [f for f in os.listdir() if f.endswith('.pdf')]
    if not files:
        print("❌ No PDF files found in this directory.")
        return []
    print("\n📂 Available PDFs:")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    return files

def main():
    files = get_pdf_files()
    if not files:
        return
    
    print("\nEnter the PDF numbers you want to merge (comma-separated, e.g., 1,3,2):")
    indexes = input(">> ").split(',')
    selected_pdfs = []

    try:
        for idx in indexes:
            selected_pdfs.append(files[int(idx.strip()) - 1])
    except:
        print("❌ Invalid selection.")
        return

    output_name = input("Enter output file name (with .pdf): ")
    merge_pdfs(selected_pdfs, output_name)

if __name__ == "__main__":
    main()
