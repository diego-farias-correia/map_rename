from pathlib import Path
from datetime import date

from map_ibge import occurrence_list

ROOT_FOLDER = Path(__file__).parent
EXE_FOLDER = ROOT_FOLDER / "files_exe"
GC_FOLDER = EXE_FOLDER / "geocode"
LINK_FOLDER = EXE_FOLDER / "link"
RELATORY_FOLDER = EXE_FOLDER / "relatory"


def create_file(str_folder="", name_file=""):
    with open(str_folder, 'w'):
        print(f"The new relatory file {name_file} has created.")    


def insert_file(*args, name_file=""):
    with open(str(RELATORY_FOLDER / name_file), 'a') as file:
        for arg in args:
            file.write(f"{arg}\n")
    return True


def mk_list(str_folder=""):
    with open(str_folder, 'r') as file:
        ref_list = [ref.rstrip("\n") for ref in file.readlines()]
    return ref_list


set_geocode = {geocode[:15] for geocode in occurrence_list if geocode[:5] != "Error"}
csv_list = []
training_map = []

for geocode in set_geocode:
    for name_file in GC_FOLDER.iterdir():
        
        gc_txt_list = mk_list(str(GC_FOLDER / name_file))
        if not geocode in gc_txt_list:
            continue
        
        try:
            
            gc_index = gc_txt_list.index(geocode)
            lk_txt_list = mk_list(str(LINK_FOLDER / name_file))
            cell_list = mk_list(str(EXE_FOLDER / "cell.txt"))
            csv_info = f"{name_file[:3]},{geocode},{lk_txt_list[gc_index]},{cell_list[gc_index]}"
            csv_list.append(csv_info)

        except ValueError as erro:
            
            training_map.append(geocode)
            print(f"The geocode ({geocode}) is not in database from Paraíba geocodes. This is a training map.")
    
    rel_name_file = f"RELATORY-{date.today()}.txt"
    tm_name_file = f"TRAININGMAP-{date.today()}.txt"

insert_file(*csv_list, name_file=rel_name_file)
insert_file(*training_map, tm_name_file)

print(f"Processo de criação concluído. Seguir para {RELATORY_FOLDER} para verificar os relatórios criados")