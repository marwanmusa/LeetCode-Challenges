import re
from pathlib import Path

def update_readme_paths():
    # Read the README.md file
    readme_path = Path('README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regular expression to find markdown links to Python files
    # Pattern: [Python](./path/to/file.py)
    pattern = r'\[Python\]\((\.\/[^)]+?\.py)\)'
    
    def replace_path(match):
        original_path = match.group(1)  # e.g., ./Unspecified/two_sum.py
        
        # Skip if already in a Python directory
        if '/Python/' in original_path:
            return match.group(0)
        
        # Create the new path by inserting 'Python/' before the filename
        parts = original_path.rsplit('/', 1)
        if len(parts) == 1:
            # Handle case where file is in root
            new_path = f"./Python/{parts[0]}"
        else:
            directory, filename = parts
            new_path = f"{directory}/Python/{filename}"
        
        return f'[Python]({new_path})'
    
    # Replace all matches
    updated_content = re.sub(pattern, replace_path, content)
    
    # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("README.md paths updated successfully!")

if __name__ == "__main__":
    update_readme_paths()