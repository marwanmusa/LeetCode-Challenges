import re
from pathlib import Path

def update_readme_paths():
    root_dir = Path(__file__).parent.parent
    readme_path = root_dir / 'README.md'
    
    # Read the current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # List of path updates (old -> new)
    path_updates = {
        './Unspecified/Python/two_sum.py': './Array-String/Python/two_sum.py',
        './Unspecified/two_sum.cpp': './Array-String/CPP/two_sum.cpp',
        './Unspecified/Python/longest_substring_without_repeating_character.py': './Array-String/Python/longest_substring_without_repeating_character.py',
        './Unspecified/Python/palindrome_number.py': './Math/Python/palindrome_number.py',
        './Unspecified/palindrome_number.cpp': './Math/CPP/palindrome_number.cpp',
        './Unspecified/Python/roman_to_int.py': './Math/Python/roman_to_int.py',
        './Queue%20&%20Stack/Python/valid_parentheses.py': './Queue-Stack/Python/valid_parentheses.py',
        './Unspecified/Python/removes_duplicates_from_sorted_arrays.py': './Array-String/Python/removes_duplicates_from_sorted_arrays.py',
        './Unspecified/Python/remove_element.py': './Array-String/Python/remove_element.py',
        './Unspecified/Python/search_in_rotated_sorted_array.py': './Array-String/Python/search_in_rotated_sorted_array.py',
        './Unspecified/Python/search_insert_position.py': './Sorting/Python/search_insert_position.py',
        './Unspecified/Python/valid_sudoku.py': './Array-String/HashTable/valid_sudoku.py',
        './Unspecified/Python/group_anagrams.py': './Array-String/Python/group_anagrams.py',
        './Unspecified/Python/maximum_subarray.py': './Array-String/Python/maximum_subarray.py',
        './Unspecified/Python/length_of_last_world.py': './Array-String/Python/length_of_last_world.py',
        './Unspecified/Python/minimum_path_sum.py': './DynamicProgramming/Python/minimum_path_sum.py',
        './combinations.py': './DynamicProgramming/Python/combinations.py',
        './Unspecified/Python/remove_duplicates_from_sorted_list.py': './Sorting/Python/remove_duplicates_from_sorted_list.py',
        './Unspecified/Python/scramble_string.py': './Array-String/Python/scramble_string.py',
        './Unspecified/Python/merge_sorted_array.py': './Array-String/Python/merge_sorted_array.py',
        './Recursion-1/validate_binary_search_tree.py': './Recursion-1/Python/validate_binary_search_tree.py',
        './BinarySearch/validate_binary_search_tree.py': './BinarySearch/Python/validate_binary_search_tree.py',
        './Unspecified/Python/sorted_array_to_BST.py': './BinaryTree/Python/sorted_array_to_bst.py'
    }
    
    # Replace paths in the content
    for old_path, new_path in path_updates.items():
        content = content.replace(old_path, new_path)
    
    # Update the categories section
    categories_section = """## 📋 Problem Categories

- Array & String (including HashTable)
- Binary Search
- Binary Tree
- Bits (Bit Manipulation)
- Concurrency
- Dynamic Programming
- Graph
- Heap
- Linked List
- Math
- N-ary Tree
- Queue & Stack
- Recursion (Part 1 & 2)
- Simulation
- Sorting
- Trie
- Two Pointers

"""
    
    # Replace the old categories section
    content = re.sub(r'## 📋 Problem Categories\n\n.*?---\n', categories_section + '---\n', content, flags=re.DOTALL)
    
    # Write the updated content back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("README.md paths and categories updated successfully!")

if __name__ == "__main__":
    update_readme_paths()