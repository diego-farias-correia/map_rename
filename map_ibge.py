import os
import sys
from pathlib import Path



ROOT_FOLDER = Path(__file__).parent
jpg_folder = "jpg"
new_folder = ROOT_FOLDER / jpg_folder
new_folder.mkdir(exist_ok= True)