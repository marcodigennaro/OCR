import cv2
import PIL
from pathlib import Path

import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
import os
from ocr.config import BASE_DIR, PDF_DIR

from pdf2image import convert_from_path
import pytesseract


class OCRHandler:
    def __init__(self):
        self.texts = None
        self.images = None
        self.pdf_path = None
        self.base_path = Path(BASE_DIR)

    def convert_pdf_to_images(self, pdf_name):
        self.pdf_path = Path(PDF_DIR).joinpath(pdf_name)
        print(self.pdf_path)
        self.images = convert_from_path(self.pdf_path)

    def perform_ocr(self):
        self.texts = [pytesseract.image_to_string(image) for image in self.images]
        return self.texts


ocr_handler = OCRHandler()
ocr_handler.convert_pdf_to_images('AXA_voiture_2024.pdf')
texts = ocr_handler.perform_ocr()
print(texts)
