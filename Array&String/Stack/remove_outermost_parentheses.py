class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, l, r, cur_idx, n = "", 0, 0, 0, len(s)
        if n == 1: return s

        for i, el in enumerate(s):

            if el == '(': l += 1
            else: r += 1

            if l == r:
                ans += s[cur_idx + 1 : i]
                cur_idx, l, r = i + 1, 0, 0

        return ans