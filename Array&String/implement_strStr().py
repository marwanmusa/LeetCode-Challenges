class Solution:
    """
    Task:
    Given two strings needle and haystack,
    return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


    # KMP algorithm
    def strStr(self, haystack, needle):

        def kmp(str_):
                b, prefix = 0, [0]
                for i in range(1, len(str_)):
                    while b > 0 and str_[i] != str_[b]:
                        b = prefix[b - 1]
                    if str_[b] == str_[i]:
                        b += 1
                    else:
                        b = 0
                    prefix.append(b)
                return prefix

        str_ = kmp(needle + '#' + haystack)
        n = len(needle)
        if n == 0:
            return n
        for i in range(n + 1, len(str_)):
            if str_[i] == n:
                return i - 2 * n
        return -1
