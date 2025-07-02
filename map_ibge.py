from pathlib import Path


ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / "pdf"
JPG_FOLDER = ROOT_FOLDER / "jpg"
ERROR_FOLDER = ROOT_FOLDER / "erro"

for day_folder in PDF_FOLDER.iterdir():
    for op_folder in day_folder.iterdir():
        print(op_folder)