class Solution:
    """
    Task:
    Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
    For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
    """
    # Using while loop
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result # chr(1+ord('A)) = B and so on.
            columnNumber //= 26 # floor division
        return result

    # Using recursion
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle((columnNumber - 1) // 26) + \
        chr(ord('A') + (columnNumber - 1) % 26) if columnNumber else ''