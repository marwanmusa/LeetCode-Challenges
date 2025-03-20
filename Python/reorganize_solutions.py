import os
import shutil
from pathlib import Path

def reorganize_solutions():
    # Root directory of the repository
    root_dir = Path('.')
    
    # Find all Python files that aren't already in a Python folder
    for py_file in root_dir.glob('**/*.py'):
        # Skip files already in Python directories
        if 'Python' in py_file.parts:
            continue
            
        # Skip special files like __init__.py
        if py_file.name.startswith('__'):
            continue
            
        # Get the category directory
        category_dir = py_file.parent
        
        # Create Python subdirectory if it doesn't exist
        python_dir = category_dir / 'Python'
        python_dir.mkdir(exist_ok=True)
        
        # New path for the file
        new_path = python_dir / py_file.name
        
        # Move the file
        print(f"Moving {py_file} to {new_path}")
        shutil.move(str(py_file), str(new_path))
    
    print("Reorganization complete!")

if __name__ == "__main__":
    reorganize_solutions()