#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def move_files():
    root_dir = Path(__file__).parent.parent
    unspecified_dir = root_dir / 'Unspecified'
    
    # Define file mappings
    file_mappings = {
        # Math files
        'palindrome_number.cpp': 'Math/CPP',
        'palindrome_number.py': 'Math/Python',
        'excel_sheet_column_number.py': 'Math/Python',
        'find_numbers_with_even_number_of_digits.py': 'Math/Python',
        'happy_number.py': 'Math/Python',
        'missing_numbers.py': 'Math/Python',
        'number_complement.py': 'Math/Python',
        'number_of_1_bits.py': 'Math/Python',
        'number_of_closed_islands.py': 'Math/Python',
        'number_of_enclaves.py': 'Math/Python',
        'number_of_steps_to_reduce_a_number_to_zero.py': 'Math/Python',
        'number_of_ways_of_cutting_a_pizza.py': 'Math/Python',
        'perfect_number.py': 'Math/Python',
        'single_number.py': 'Math/Python',
        'third_maximum_number.py': 'Math/Python',
        'ugly_number.py': 'Math/Python',

        # Array-String files
        'add_strings.py': 'Array-String/Python',
        'array_partition.py': 'Array-String/Python',
        'find_all_numbers_disappeared_in_an_array.py': 'Array-String/Python',
        'intersection_of_two_arrays.py': 'Array-String/Python',
        'intersection_of_two_arrays2.py': 'Array-String/Python',
        'isomorphic_strings.py': 'Array-String/Python',
        'longest_substring_without_repeating_character.py': 'Array-String/Python',
        'maximum_subarray.py': 'Array-String/Python',
        'merge_sorted_array.py': 'Array-String/Python',
        'minimize_maximum_of_array.py': 'Array-String/Python',
        'minimum_size_subarray_sum.py': 'Array-String/Python',
        'number_of_segments_in_a_string.py': 'Array-String/Python',
        'number_of_zero_filled_subarray.py': 'Array-String/Python',
        'optimal_partition_of_string.py': 'Array-String/Python',
        'permutation_in_string.py': 'Array-String/Python',
        'removes_duplicates_from_sorted_arrays.py': 'Array-String/Python',
        'repeated_substring_pattern.py': 'Array-String/Python',
        'reverse_vowels_of_string.py': 'Array-String/Python',
        'reverse_word_in_string.py': 'Array-String/Python',
        'reverse_word_in_string_iii.py': 'Array-String/Python',
        'rotate_array.py': 'Array-String/Python',
        'running_sum_of_1d_array.py': 'Array-String/Python',
        'scramble_string.py': 'Array-String/Python',
        'search_in_rotated_sorted_array.py': 'Array-String/Python',
        'sorted_array_to_bst.py': 'Array-String/Python',
        'squares_of_sorted_array.py': 'Array-String/Python',

        # BinaryTree files
        'balanced_binary_tree.py': 'BinaryTree/Python',
        'binary_watch.py': 'BinaryTree/Python',
        'bst_lowest_common_ancestor.py': 'BinaryTree/Python',
        'find_duplicate_subtrees.py': 'BinaryTree/Python',
        'insert_into_a_binary_search_tree.py': 'BinaryTree/Python',
        'invert_binary_tree.py': 'BinaryTree/Python',
        'merge_two_binary_trees.py': 'BinaryTree/Python',
        'min_depth_of_binary_tree.py': 'BinaryTree/Python',
        'two_sum_iv_input_is_a_bst.py': 'BinaryTree/Python',

        # HashTable files
        'design_hashmap.py': 'Array-String/HashTable',
        'design_hashset.py': 'Array-String/HashTable',

        # Sorting files
        'remove_duplicates_from_sorted_list.py': 'Sorting/Python',
        'search_insert_position.py': 'Sorting/Python',

        # Bits files
        'counting_bits.py': 'Bits/Python',
        'reverse_bits.py': 'Bits/Python',

        # LinkedList files
        'middle_of_linked_list.py': 'LinkedList/Python',

        # Two Sum (special case - commonly used as example)
        'two_sum.cpp': 'Array-String/CPP',
        'two_sum.py': 'Array-String/Python',
    }

    # Move each file to its new location
    for filename, new_category in file_mappings.items():
        src = unspecified_dir / filename
        if src.exists():
            dst = root_dir / new_category / filename
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(src), str(dst))
                print(f"Moved {filename} to {new_category}/")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

if __name__ == "__main__":
    move_files()
