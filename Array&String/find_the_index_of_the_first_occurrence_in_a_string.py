class Solution:
    """
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.
    """
    # Method 1
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h < n: return -1
        count = 0
        for i in range(h):
            if haystack[i] == needle[0] and (i + n <= h):
                for j in range(i, i+n):
                    if haystack[j] and (haystack[j] == needle[j-i]):
                        count += 1
                    if haystack[j] and (haystack[j] != needle[j-i]):
                        break
                # print(count, n)
                if count == n:
                    return i
                count = 0
        return -1


    # Method 2
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        run = len(needle)

        for idx in range(len(haystack) - run + 1):
            if needle == haystack[idx:idx+run]:
                return idx

        return index


    # Method 3 using built-in function
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


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