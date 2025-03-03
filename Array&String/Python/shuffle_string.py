class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = list(s)
        for i, v in enumerate(indices): res[v] = s[i]
        return ''.join(res)