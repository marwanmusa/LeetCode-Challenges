class Solution:
    """
    Task:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    def isPalindrome(self, s: str) -> bool:
        # check if the letter is alphanumeric using isalnum()
        # join all letters if isalnum() == true
        s = ''.join(i for i in s.lower() if i.isalnum())
        return s == s[::-1] # True if s = its reverse