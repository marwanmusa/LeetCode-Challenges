class Solution:
    """
    Task:
    Given a string columnTitle that represents the column title as appears in an Excel sheet,
    return its corresponding column number.
    """
    # First I made a list of alphabet
    # then make pair of each word with its val
    def titleToNumber(self, columnTitle: str) -> int:
        words = [chr(i).upper() for i in range(97, 123)]
        word_val = {words[val]: val+1 for val in range(len(words))}
        res = 0
        for i in range(len(columnTitle)):
            res += word_val[columnTitle[::-1][i]]*(26**i)
        return res

    # more efficient way
    # we can use ord(alphabet)-64 instead
    # since ord('A') == 65, ord('B') == 66 and so on
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        columnNumber = 0
        for i in range(len(columnTitle)):
            columnNumber += (ord(columnTitle[i]) - 64) * (26 ** i)
        return columnNumber