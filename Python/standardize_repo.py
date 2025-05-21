#!/usr/bin/env python3
import os
import re
from pathlib import Path

def standardize_filename(filename):
    """Convert a filename to standard format: problem_name.ext"""
    # Remove any version numbers from filename first
    name, ext = os.path.splitext(filename)
    
    # Convert to lowercase and replace spaces/special chars with underscore
    name = re.sub(r'[^\w\s-]', '', name.lower())
    name = re.sub(r'[\s-]+', '_', name)
    
    # Remove any double underscores
    name = re.sub(r'_+', '_', name)
    
    # Add extension back
    return f"{name}{ext}"

def process_solutions(root_dir):
    """Process all solution files in the repository"""
    changes = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(('.py', '.cpp', '.js')):
                old_path = os.path.join(dirpath, filename)
                new_filename = standardize_filename(filename)
                new_path = os.path.join(dirpath, new_filename)
                
                if new_filename != filename:
                    try:
                        os.rename(old_path, new_path)
                        changes.append((old_path, new_path))
                    except Exception as e:
                        print(f"Error renaming {old_path}: {e}")
    return changes

def update_readme(readme_path, changes):
    """Update the README.md file with new file paths"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update directory references
    content = content.replace('Array&String', 'Array-String')
    content = content.replace('Queue & Stack', 'Queue-Stack')
    
    # Update file paths
    for old_path, new_path in changes:
        old_rel = os.path.relpath(old_path, os.path.dirname(readme_path))
        new_rel = os.path.relpath(new_path, os.path.dirname(readme_path))
        content = content.replace(old_rel, new_rel)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

def categorize_unspecified(root_dir):
    """Suggest categories for files in Unspecified directory"""
    unspecified_dir = os.path.join(root_dir, 'Unspecified')
    if not os.path.exists(unspecified_dir):
        return
    
    category_patterns = {
        r'array|string|substr': 'Array-String',
        r'tree|bst|binary': 'BinaryTree',
        r'search|sort': 'Sorting',
        r'linked.*list': 'LinkedList',
        r'stack|queue': 'Queue-Stack',
        r'hash|map|set': 'HashTable',
        r'dynamic|dp': 'DynamicProgramming',
        r'math|number|calculate': 'Math',
        r'bit|binary': 'Bits',
    }
    
    suggestions = {}
    for root, _, files in os.walk(unspecified_dir):
        for filename in files:
            if filename.endswith(('.py', '.cpp', '.js')):
                for pattern, category in category_patterns.items():
                    if re.search(pattern, filename.lower()):
                        suggestions[filename] = category
                        break
    return suggestions

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.dirname(__file__))
    readme_path = os.path.join(root_dir, 'README.md')
    
    # Process files
    changes = process_solutions(root_dir)
    if changes:
        print("Files renamed:")
        for old, new in changes:
            print(f"{old} -> {new}")
        
        # Update README
        update_readme(readme_path, changes)
        print("\nREADME.md updated with new paths")
    
    # Suggest categories for unspecified files
    suggestions = categorize_unspecified(root_dir)
    if suggestions:
        print("\nSuggested categories for files in Unspecified/:")
        for filename, category in suggestions.items():
            print(f"{filename} -> {category}/")
