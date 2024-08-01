import cv2
import PIL
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
import os

from classes import OCRHandler

ocr_handler = OCRHandler()
ocr_handler.convert_pdf_to_images('AXA_voiture_2024.pdf')
texts = ocr_handler.perform_ocr()
print(texts)
