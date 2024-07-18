import shutil
import os
from pathlib import Path

current_root = Path().resolve()
folder_path = current_root / 'temp'

try:
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Successfully deleted folder: {folder_path}")
    else:
        print(f"Folder does not exist: {folder_path}")
except Exception as e:
            print(f"Folder cannot does not exist: {folder_path}")

