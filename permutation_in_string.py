from collections import Counter

class Solution:
    """
    Task:
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.
    """
    # Method 1, using two pointer and counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charSet = set()
        l = 0
        k = len(s1)
        r = k
        while l < r and r <= len(s2):
            subs = s2[l:r]
            # print(subs)
            if Counter(s1) == Counter(subs):
                return True
            l += 1
            r += 1
        return False


    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2) : return False
    #     s1Count, s2Count = [0]*26, [0]*26
    #     for i in range(len(s1)):
    #         s1Count[ord(s1[i]) - ord('a')] += 1
    #         s2Count[ord(s2[i]) - ord('a')] += 1

    #     matches =  0
    #     for i in range(26):
    #         matches += (1 if s1Count[i] == s2Count[i] else 0)

    #     l = 0
    #     for r in range(len(s1), len(s2)):
    #         if matches == 26: return True

    #         index = ord(s2[r]) - ord('a')
    #         s2Count[index] += 1
    #         if s1Count[index] == s2Count[index]:
    #             matches += 1
    #         elif s1Count[index] + 1 == s2Count[index]:
    #             matches -= 1

    #         index = ord(s2[l]) - ord('a')
    #         s2Count[index] -= 1
    #         if s1Count[index] == s2Count[index]:
    #             matches += 1
    #         elif s1Count[index] + 1 == s2Count[index]:
    #             matches -= 1
    #         l += 1
    #     return matches == 26

    # Method 2, sliding window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
        matchTarget = len([i for i in s1Count if i!=0])

        s1Count = [None if i==0 else i for i in s1Count]

        winlen, matched = len(s1), 0

        for i in range(len(s2)):
            index = ord(s2[i]) - ord("a")
            if s1Count[index] != None:
                s1Count[index] -= 1
                if s1Count[index] == 0:
                    matched += 1

            if i - winlen >= 0:
                index = ord(s2[i-winlen]) - ord("a")
                if s1Count[index] != None:
                    if s1Count[index] == 0:
                        matched -= 1
                    s1Count[index] += 1

            if matched == matchTarget:
                return True

        return False