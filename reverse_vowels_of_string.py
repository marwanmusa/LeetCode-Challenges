class Solution:
    """
    Task:
    Given a string s, reverse only all the vowels in the string and return it.
    ls are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
    """
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = 'aeiouAEIOU'
        l, r = 0, len(s) - 1

        while (l < r):
            while (l < r and s[l] not in vowels):
                l += 1
            while (r > l and s[r] not in vowels):
                r -= 1
            s [l], s[r] = s[r], s[l]

            l +=1
            r -=1

        return "".join(s)