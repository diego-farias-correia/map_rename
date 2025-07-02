import cv2 as cv
import pytesseract as pt
from pdf2image import convert_from_path
from pathlib import Path
from PIL import Image


ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / "pdf"
JPG_FOLDER = ROOT_FOLDER / "jpg"
ERROR_FOLDER = ROOT_FOLDER / "erro"

POP_PATH = ROOT_FOLDER / "poppler-24.08.0" / "Library" / "bin"
TESSERACT_PATH = ROOT_FOLDER / "Tesseract-OCR" / "tesseract.exe"
pt.pytesseract.tesseract_cmd = TESSERACT_PATH


def convert_pdf(path_pdf):
    pdf = convert_from_path(path_pdf, poppler_path=str(POP_PATH))
    for pag in pdf:
        pag_name = f"imagem-{pdf.index(pag)+1}.jpg"
        pag.save(str(JPG_FOLDER / pag_name), "JPEG")


def street_satellite(path_jpg):
    count_pxl = 0
    for cut in range(200, 700, 50):
        red, blue, green = cv.imread(path_jpg)[cut, 700]
        if red == blue == green:
            count_pxl += 1
        if count_pxl > 4:
            return 'm'
        return 'i'


for day_folder in PDF_FOLDER.iterdir():
    for op_folder in day_folder.iterdir():
        print(op_folder)        
        convert_pdf(str(op_folder))

        text = pt.image_to_string(cv.imread(str(JPG_FOLDER / "imagem-2.jpg")))
        index_gc = text.find(" = ")
        gc_compose = [text[a_gc] for a_gc in range(index_gc+3, index_gc+18)]
        
        geocode = ''.join(gc_compose)
        image_type = street_satellite(str(JPG_FOLDER / "imagem-1.jpg"))

        new_name_file = f"{geocode}-{image_type}"
