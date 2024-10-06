import os

# This file gives the list of files in the project directory in a tree-like format

def list_files(startpath, exclude_folders=None):
    if exclude_folders is None:
        exclude_folders = []
    for root, dirs, files in os.walk(startpath):
        # Skip excluded folders
        if any(excluded in root for excluded in exclude_folders):
            continue
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

# Specify your project directory and the folders you want to exclude
project_directory = '.'  # Change if needed\
exclude_folders = ['Fabric_Detection_Project.egg-info', 'fabric_venv', 'laptop_notebooks',".git"]  # Add your virtual environment and image folders here

list_files(project_directory, exclude_folders)
