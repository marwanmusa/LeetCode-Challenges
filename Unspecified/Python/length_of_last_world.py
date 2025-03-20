class Solution:
    """
    Task:
    Given a string s consisting of words and spaces,
    return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.
    """
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


    # Under Construction
    # I've tried to solve the task using loop
    """
    def lengthOfLastWord(self, s: str) -> int:
        total = int()
        if len(s) == 1:
            if s[0] != " ":
                return len(s)
            else:
                return total
        else:
            i = -1
            while i >= -len(s):
                if i == -len(s):
                    if s[i] != " ":
                        total += 1
                        break
                    else:
                        break
                else:
                    if s[i] != " " and s[i - 1] == " ":
                        break
                    elif s[i] == " " and s[i - 1] == " ":
                        pass
                    elif s[i] != " ":
                        total += 1
                i -= 1
            return total + 1
        """