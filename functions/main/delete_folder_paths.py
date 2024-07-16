import shutil
import os

def delete_folder(folder_path):
    folders_to_delete = [
    'table_list',
    'temp',
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

# Example usage

