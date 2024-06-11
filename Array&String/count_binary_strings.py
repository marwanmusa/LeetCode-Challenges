class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        chunks, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i-1])
        return res
    
    # O(1) space
    def countBinarySubstrings(self, s: str) -> int:
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(prev, cur)
                prev = cur
                cur = 1
        res += min(prev, cur)
        return res