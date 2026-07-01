"""
resume_parser.py

Unified Resume Parser

Supports:
- PDF
- DOCX

Returns cleaned text ready for Gemini.
"""

from pathlib import Path
import pdfplumber
from docx import Document


class ResumeParser:

    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file
        self.extension = Path(uploaded_file.name).suffix.lower()

    # -----------------------------------------
    # Public Function
    # -----------------------------------------

    def extract_text(self):

        if self.extension == ".pdf":
            return self._extract_pdf()

        elif self.extension == ".docx":
            return self._extract_docx()

        raise ValueError(
            f"Unsupported file format: {self.extension}"
        )

    # -----------------------------------------
    # PDF Extraction
    # -----------------------------------------

    def _extract_pdf(self):

        text = ""

        with pdfplumber.open(self.uploaded_file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return self._clean(text)

    # -----------------------------------------
    # DOCX Extraction
    # -----------------------------------------

    def _extract_docx(self):

        document = Document(self.uploaded_file)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return self._clean(text)

    # -----------------------------------------
    # Cleaning
    # -----------------------------------------

    def _clean(self, text):

        cleaned = []

        for line in text.splitlines():

            line = line.strip()

            if line:

                cleaned.append(line)

        return "\n".join(cleaned)