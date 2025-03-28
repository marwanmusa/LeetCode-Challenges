class Solution:
    def reformat(self, s: str) -> str:
        ans, digit, alpha = "", "", ""

        for w in s:
            if w.isalpha(): alpha += w
            else: digit += w

        if abs(len(digit) - len(alpha)) > 1: return ""

        if len(alpha) > len(digit): digit, alpha = alpha, digit

        for i in range(len(alpha)):
            ans += digit[i]
            ans += alpha[i]

        if len(alpha) < len(digit): ans += digit[-1]

        return ans