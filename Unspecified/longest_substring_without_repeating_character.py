class Solution:
    """
    Task:
    Given a string s, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res


    # optimized solution using dict
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_len, start, chars = 0, -1, {}
        for i, v in enumerate(s):
            if v in chars and chars[v] > start:
                start = chars[v]
            elif i-start > longest_len:
                longest_len = i-start
            chars[v] = i