class Solution:
    """
    Task:
    Given a string s, reverse the order of characters in each word
    within a sentence while still preserving whitespace and initial word order.
    """
    # Method 1
    def reverseWords(self, s: str) -> str:
        s = s[::-1].split()
        s.reverse()
        s = ' '.join(s)
        return s

    # Method 2
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda word: word[::-1], s.split(' '))))