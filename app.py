import subprocess

def convert_tex_to_pdf(tex_file_path):
    try:
        # Run pdflatex command to convert .tex to .pdf
        subprocess.run(['pdflatex', tex_file_path])
        print("PDF conversion successful!")
    except Exception as e:
        print(f"PDF conversion failed: {e}")

# Example usage
tex_file_path = 'main.tex'  # Replace 'example.tex' with your actual .tex file path
convert_tex_to_pdf(tex_file_path)
