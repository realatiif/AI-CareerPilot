from pypdf import PdfReader
from docx import Document


def extract_resume_text(uploaded_file):
    """Extract readable text from PDF or DOCX."""

    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        parts = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                parts.append(text)

        return "\n".join(parts).strip()

    if name.endswith(".docx"):
        document = Document(uploaded_file)
        parts = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]
        return "\n".join(parts).strip()

    raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")
