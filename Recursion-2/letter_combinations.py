from functools import reduce

# mapping of digits to letters
map_num = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution:
    """
    Task:
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations
    that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    """

    # approach using list comprehension
    def letterCombinations(self, digits: str) -> list[str]:
        # create a mapping of digits to letters as a list
        map_num = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # initialize the combinations list with an empty string if digits is not empty,
        # otherwise initialize it as an empty list
        comb = [''] if digits else []
        # iterate over each digit in digits
        for d in digits:
            # generate all possible combinations by adding each letter in the current digit
            # to each of the previous combinations
            comb = [p + q for p in comb for q in map_num[d]]
        # return the final list of combinations
        return comb

    # backtracking approach
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        # recursive function to generate all possible combinations using backtracking
        def backtrack(i, cur):
            # base case: if we have reached the end of the digits string
            if i == len(digits):
                # if the current combination is not empty, add it to the result list
                if len(cur) > 0: res.append(''.join(cur))
                return
            # iterate over each letter in the current digit
            for c in map_num[digits[i]]:
                # recursively generate combinations by adding the current letter to the current combination
                backtrack(i+1, cur+[c])
        # start the backtracking process with an empty combination
        backtrack(0, [])
        # return the final list of combinations
        return res

    # approach using reduce function
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        # use reduce function to generate all possible combinations
        return reduce(lambda acc, digit: [x+y for x in acc for y in map_num[digit]], digits, [''])