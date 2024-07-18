@echo off

rem Set the directory for the Python cache
set PYTHONPYCACHEPREFIX=.\pycache\

rem Run the first Python script
.\embed\python main.py

rem Run the second Python script
.\embed\python delete_folder_paths.py

pause
