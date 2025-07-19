import shutil
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
    if len(pdf) == 1:
        return True
    for pag in pdf:
        pag_name = f"image-{pdf.index(pag)+1}.jpg"
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


def try_new_angule():
    original_image = Image.open(str(JPG_FOLDER / "image-2.jpg"))
    hor_image = original_image.resize((2339, 3307)).rotate(-90, expand=True)
    hor_image.save(str(JPG_FOLDER / "image-2.jpg"))
    original_image.close()


def try_geocode(compose):
    if len(compose) == 15:
        return compose
    return "Error-name"


folder_list = list(PDF_FOLDER.iterdir())
total_folder = len(folder_list)

occurrence_list = []
for folder_progress, day_folder in enumerate(folder_list, start=1):
    
    print(f"Actual progress: {(folder_progress/total_folder)*100}% of folders...")
    list_file = list(day_folder.iterdir())
    total_files = len(list_file)

    for pdf_progress, op_folder in enumerate(list_file, start=1):

        print(f"Actual progress: {(pdf_progress/total_files)*100}% of files...")
        print(f" Work in file: {op_folder.name}")

        white_page = convert_pdf(str(op_folder))
        if white_page is True:
            continue

        try:
            for rotation in range(0, 5):

                text_gc = pt.image_to_string(cv.imread(str(JPG_FOLDER / "image-2.jpg")))
                index_gc = text_gc.find(" = ")
                gc_compose = [text_gc[d_gc] for d_gc in range(index_gc+3, index_gc+18) if text_gc[d_gc].isnumeric()]
                geocode = try_geocode(''.join(gc_compose))
                
                if geocode != "Error-name":
                    break
                try_new_angule()

            image_type = street_satellite(str(JPG_FOLDER / "image-1.jpg"))
            new_name_file = f"{geocode}-{image_type}"

        except IndexError:
            geocode = "Error-pag2"
            print("Error in the second page! SCAN IN STANDARD POSITION")

        new_name_file = f"{geocode}-{image_type}"


        if new_name_file.split('-')[0] in occurrence_list:
            new_name_file = f"{new_name_file}-{occurrence_list.count(new_name_file.split('-')[0])}"
        
        occurrence_list.append(new_name_file.split('-')[0])
        
        rename_sintaxe = op_folder.parent / f"{new_name_file}.pdf"
        op_folder.rename(rename_sintaxe)
        print(f"The file {new_name_file} has succesfull renamed")

        if new_name_file[:5] == "Error":
            print(str(op_folder.parent / f"{new_name_file}.pdf"))
            print(str(ERROR_FOLDER / f"{new_name_file}.pdf"))
            shutil.move(op_folder.parent / f"{new_name_file}.pdf", ERROR_FOLDER / f"{new_name_file}.pdf")
            print(f"The error file {new_name_file} is moved to {ERROR_FOLDER}.")

for files in JPG_FOLDER.iterdir():
    files.unlink()

print("Initializing relatory generate...")

import json
from datetime import date

EXE_FOLDER = ROOT_FOLDER / "files_exe"
RELATORY_FOLDER = EXE_FOLDER / "relatory"


def create_file(name_file=""):
    with open(str(RELATORY_FOLDER / name_file), 'w'):
        print(f"The new relatory file {name_file} has created.")    


def insert_file(*args, name_file=""):
    with open(str(RELATORY_FOLDER / name_file), 'a') as file:
        for arg in args:
            file.write(f"{arg}\n")


set_geocode = {geocode[:15] for geocode in occurrence_list if geocode[:5] != "Error"}
with open(str(EXE_FOLDER / "base.json"), 'r') as file:
    dict_base = json.load(file)

training_map = [geocode for geocode in set_geocode if geocode[:2] != '25']
csv_list = [dict_base[geocode] for geocode in set_geocode if geocode[:2] == '25']

rel_name_file = f"RELATORY-{date.today()}.txt"
create_file(rel_name_file)
insert_file(*csv_list, name_file=rel_name_file)

if len(training_map)>1:
    tm_name_file = f"TRAININGMAP-{date.today()}.txt"
    create_file(tm_name_file)
    insert_file(*training_map, tm_name_file)

print(f"Processo de criação concluído. Seguir para {RELATORY_FOLDER} para verificar os relatórios criados")
