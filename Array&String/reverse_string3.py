class Solution:
    """
    Task:
    Given a string s, reverse the order of characters in each word within a sentence
    while still preserving whitespace and initial word order.
    """
    def reverseWords(self, s: str) -> str:
        ans = ""
        for w in s.split(" "):
            ans += w[::-1]
            ans += ' '
        return ans.strip()
    

    # one-line
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])