class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        i, j, ans = 0, len(s), []
        for char in s:
            if char == 'D':
                ans.append(j)
                j -= 1
            else:
                ans.append(i)
                i += 1
        ans.append(i)
        return ans