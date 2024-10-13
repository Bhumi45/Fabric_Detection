import os
"""
This script is used to generate a tree structure of the project directory
"""
def list_files(startpath, exclude_folders=None, output_file=None):
    if exclude_folders is None:
        exclude_folders = []
    
    # Normalize exclude folders to absolute paths for comparison
    exclude_folders = [os.path.abspath(os.path.join(startpath, excluded)) for excluded in exclude_folders]
    
    if output_file:
        with open(output_file, 'w') as f:
            _list_files_to_stream(startpath, exclude_folders, f.write)
    else:
        _list_files_to_stream(startpath, exclude_folders, print)

def _list_files_to_stream(startpath, exclude_folders, stream_func):
    startpath = os.path.abspath(startpath)  # Normalize the start path
    for root, dirs, files in os.walk(startpath):
        # Skip excluded folders by checking if the root matches any exclude paths
        root_path = os.path.abspath(root)
        if any(root_path.startswith(excluded) for excluded in exclude_folders):
            continue
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        stream_func(f'{indent}{os.path.basename(root)}/\n')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            stream_func(f'{subindent}{f}\n')

# Specify your project directory and the folders you want to exclude
project_directory = '.'  # Change if needed
exclude_folders = [
    'Fabric_Detection_Project.egg-info', "data", "logs", 'fabric_venv', ".git",
    "laptop_notebooks/Extracted_features", "laptop_notebooks/textures 3",
    "laptop_notebooks/Feature Extraction Techniques Trials/Augmented_images",
    "laptop_notebooks/Feature Extraction Techniques Trials/textures 3",
    "training", "deployment","artifacts","__pycache__"
]

list_files(project_directory, exclude_folders, output_file="tree_structure.txt")  # Set output_file to 'tree_structure.txt' to write to file
