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

def force_delete_directory(folder_path, file_process_error_log_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Successfully deleted folder: {folder_path}")
        else:
            print(f"Folder does not exist: {folder_path}")
    except Exception as e:
        with file_process_error_log_path.open('a', encoding='utf-8') as error_log:
            error_log.write(f'{current_time} - Error in log_file_analysis.py/force_delete_directory function: {e}\n')    