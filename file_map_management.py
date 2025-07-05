from pathlib import Path
from datetime import date

from map_ibge import occurrence_list

ROOT_FOLDER = Path(__file__).parent
EXE_FOLDER = ROOT_FOLDER / "files_exe"
GC_FOLDER = EXE_FOLDER / "geocode"
LINK_FOLDER = EXE_FOLDER / "link"
RELATORY_FOLDER = EXE_FOLDER / "relatory"

list_geocode = [geocode for geocode in occurrence_list if geocode[:5] != "Error"]
list_error = [error for error in occurrence_list if error[:5] == "Error"]

def create_file(*args, name_file=""):
    with open(str(RELATORY_FOLDER / name_file), 'a') as file:
        for arg in args:
            file.write(f"{arg}\n")
    return True

