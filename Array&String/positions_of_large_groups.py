import re

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        start = end = 0
        cur, ans, maxe = s[0], [], 2
        for i, e in enumerate(s):
            if e != cur:
                if end - start >= maxe:
                    ans.append([start, end])
                start = end = i
                cur = e
            else:
                end = i
        if start != end and end - start >= maxe:
                    ans.append([start, end])
        return ans
    
    # shorter 
    def largeGroupPositions(self, S: str) -> list[list[int]]:
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: j += 1
            if j - i >= 3: res.append([i, j - 1])
            i = j
        return res
    
    # using regex
    def largeGroupPositions(self, S: str) -> list[list[int]]:
        return [[r.start(), r.end() - 1] for r in re.finditer(r'(\w)\1{2,}', S)]