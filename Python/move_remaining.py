#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def move_remaining_files():
    root_dir = Path(__file__).parent.parent
    unspecified_dir = root_dir / 'Unspecified' / 'Python'
    
    # Define file mappings for remaining files
    file_mappings = {
        # Array-String
        'remove_element.py': 'Array-String/Python',
        'replace_elements_with_greatest_element_on_right_side.py': 'Array-String/Python',
        'two_sum_ii.py': 'Array-String/Python',
        'valid_anagram.py': 'Array-String/Python',
        'word_pattern.py': 'Array-String/Python',
        'valid_palindrome.py': 'Array-String/Python',
        'move_zeroes.py': 'Array-String/Python',
        'matrix_reshape.py': 'Array-String/Python',
        'next_greater_element_1.py': 'Array-String/Python',
        'height_checker.py': 'Array-String/Python',
        'duplicate_zeros.py': 'Array-String/Python',
        'richest_customer_wealth.py': 'Array-String/Python',
        'can_place_flowers.py': 'Array-String/Python',
        'boats_to_save_people.py': 'Array-String/Python',
        'first_unique_char.py': 'Array-String/Python',
        'jewels_and_stones.py': 'Array-String/Python',
        'assign_cookies.py': 'Array-String/Python',
        'is_subsequence.py': 'Array-String/Python',
        'keyboard_row.py': 'Array-String/Python',
        'length_of_last_world.py': 'Array-String/Python',
        'letter_case_permutation.py': 'Array-String/Python',
        'longest_palindrome.py': 'Array-String/Python',
        'summary_ranges.py': 'Array-String/Python',
        'group_anagrams.py': 'Array-String/Python',

        # Math
        'add_digits.py': 'Math/Python',
        'base7.py': 'Math/Python',
        'construct_the_rectangle.py': 'Math/Python',
        'convert_num_to_hexadecimal.py': 'Math/Python',
        'excel_sheet_column_title.py': 'Math/Python',
        'fizz_buzz.py': 'Math/Python',
        'nim_game.py': 'Math/Python',
        'power_of_four.py': 'Math/Python',
        'power_of_three.py': 'Math/Python',
        'power_of_two.py': 'Math/Python',
        'roman_to_int.py': 'Math/Python',
        'relative_ranks.py': 'Math/Python',

        # Dynamic Programming
        'house_robber.py': 'DynamicProgramming/Python',
        'minimum_path_sum.py': 'DynamicProgramming/Python',
        'minimum_costs_for_tickets.py': 'DynamicProgramming/Python',
        'range_sum_query_immutable.py': 'DynamicProgramming/Python',
        'reducing_dishes.py': 'DynamicProgramming/Python',
        'triangle.py': 'DynamicProgramming/Python',

        # Graph problems
        'count_unreacheable_pairs_of_nodes_in_an_undirected_graph.py': 'Graph/Python',
        'longest_cycle_in_a_graph.py': 'Graph/Python',
        'reorder_routes_to_make_all_paths_lead_to_city_zero.py': 'Graph/Python',
        'rotting_oranges.py': 'Graph/Python',
        'max_area_of_island.py': 'Graph/Python',
        'island_perimeter.py': 'Graph/Python',
        'minimum_score_of_a_path_between_two_cities.py': 'Graph/Python',

        # HashTable
        'contains_duplicate.py': 'Array-String/HashTable',
        'contains_duplicate2.py': 'Array-String/HashTable',
        'distribute_candies.py': 'Array-String/HashTable',
        'find_the_difference.py': 'Array-String/HashTable',
        'hamming_distance.py': 'Array-String/HashTable',
        'insert_delete_getrandom_o1.py': 'Array-String/HashTable',
        'minimum_index_sum_of_two_lists.py': 'Array-String/HashTable',
        'ransom_note.py': 'Array-String/HashTable',
        'valid_sudoku.py': 'Array-String/HashTable',
        'top_k_freq_element.py': 'Array-String/HashTable',

        # BinaryTree
        'populating_next_right_pointers.py': 'BinaryTree/Python',
        'root_equals_sum_of_children.py': 'BinaryTree/Python',

        # Other files that need categorization
        'combinations.py': 'DynamicProgramming/Python',  # Could also be Backtracking
        'detect_capital.py': 'Array-String/Python',
        'licensing_key_formatting.py': 'Array-String/Python',
        'majority_element.py': 'Array-String/Python',
        'max_consecutive_ones.py': 'Array-String/Python',
        'buy_and_sell_stock.py': 'DynamicProgramming/Python',
        'teemo_attacking.py': 'Simulation/Python',
        'check_if_n_and_its_double_exist.py': 'Array-String/Python',
        '4sum_ii.py': 'Array-String/Python',
    }

    # Create Graph directory if it doesn't exist
    (root_dir / 'Graph' / 'Python').mkdir(parents=True, exist_ok=True)

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
    move_remaining_files()
