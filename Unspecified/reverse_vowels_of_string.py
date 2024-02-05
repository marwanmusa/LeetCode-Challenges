class Solution:
    """
    Task:
    Given a string s, reverse only all the vowels in the string and return it.
    ls are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
    """
    # Method 1
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


    # Method 2
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','A','e','E','i','I','o','O','u','U'}
        s = list(s)

        ### extract all vowels from s
        vowelInS = [c for c in s if c in vowels]

        ### replace the vowels in s with the reversed ones
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowelInS.pop(-1)

        return ''.join(s)