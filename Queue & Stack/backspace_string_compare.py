class Solution:
    """
    Task:
        Given two strings s and t, return true if they are equal when both are typed into empty text editors.
        '#' means a backspace character.

        Note that after backspacing an empty text, the text will continue empty.
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(s):
            j = ""
            for e in s:
                if e != '#': j += e
                else:
                    if j: j = j[:-1]
            return j
        return stack(s) == stack(t)