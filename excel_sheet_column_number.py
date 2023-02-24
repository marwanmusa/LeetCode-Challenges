class Solution:
    """
    Task:
    Given a string columnTitle that represents the column title as appears in an Excel sheet,
    return its corresponding column number.
    """
    def titleToNumber(self, columnTitle: str) -> int:
        words = [chr(i).upper() for i in range(97, 123)]
        word_val = {words[val]: val+1 for val in range(len(words))}
        res = 0
        for i in range(len(columnTitle)):
            res += word_val[columnTitle[::-1][i]]*(26**i)
        return res