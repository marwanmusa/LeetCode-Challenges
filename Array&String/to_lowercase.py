class Solution:
    """
    Task:
    Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
    """
    # 1, using string method
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    

    # using ASCII
    def toLowerCase(self, s: str) -> str:
        return ''.join([chr(ord(x)+32) if 65 <= ord(x) <= 90 else x for x in s])
        