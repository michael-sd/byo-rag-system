import fitz
import os

class PdfFileLoader:
    def __init__(self, path: str):
        self.documents = []
        self.path = path

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".pdf"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .pdf file."
            )

    def load_file(self):
        doc = fitz.open(self.path)
        text = ''
        for page in doc:
            text += page.get_text()
        self.documents.append(text)
        doc.close()

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".pdf"):
                    doc = fitz.open(os.path.join(root, file))
                    text = ''
                    for page in doc:
                        text += page.get_text()
                    self.documents.append(text)
                    doc.close()

    def load_documents(self):
        self.load()
        return self.documents