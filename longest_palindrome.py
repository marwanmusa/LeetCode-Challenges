class Solution(object):
    """
    Task:
    Given a string s which consists of lowercase or uppercase letters,
    return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
    """
    def longestPalindrome(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)