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
    def letterCombinations(self, digits: str) -> list[str]:
        comb = [''] if digits else []
        for d in digits:
            comb = [p + q for p in comb for q in map_num[d]]
        return comb
    
    # backtracking
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        def backtrack(i, cur):
            if i == len(digits):
                if len(cur) > 0: res.append(''.join(cur))
                return
            for c in map_num[digits[i]]:
                cur.append(c)
                backtrack(i+1, cur)
                cur.pop()
        backtrack(0, [])
        return res
        