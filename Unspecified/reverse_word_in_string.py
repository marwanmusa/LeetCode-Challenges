class Solution:
    """
    Task:
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters.
    The words in s will be separated by at least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words.
    The returned string should only have a single space separating the words.
    Do not include any extra spaces.
    """
    # Method 1
    def reverseWords(self, s: str) -> str:
        reversed = ""
        s = s.split()
        i = 0
        j = len(s)-1
        while i < len(s)//2 and i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        for i in range(len(s)):
            reversed += s[i]
            if i < len(s)-1:
                reversed += " "

        return reversed


    # Method 2
    def reverseWords(self, s: str) -> str:
        s = s.split()
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return ' '.join(s)