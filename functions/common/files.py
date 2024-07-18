import os
import shutil
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def read_file_to_array(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")
    
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:  
        for line in file:
            stripped_line = line.strip()
            lines.append(stripped_line)
       
    return lines

def delete_folder(folder_path):
    folders_to_delete = [
    'table_list',
    'view_table_list',
    'excel'
 ]
    try:
        for folder in folders_to_delete:
            full_path = os.path.join(folder_path, folder)
            if os.path.exists(full_path):
                shutil.rmtree(full_path)
                print(f"Successfully deleted folder: {full_path}")

    except Exception as e:
        print(f"Error deleting folder {full_path}: {e}")