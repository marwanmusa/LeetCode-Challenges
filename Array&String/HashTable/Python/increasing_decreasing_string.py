class Solution:
    def sortString(self, s: str) -> str:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - 97] += 1

        remaining = len(s)
        res = ""

        while remaining:
            for i in range(len(chars)):
                if chars[i] > 0:
                    res += chr(i + 97)
                    chars[i] -= 1
                    remaining -= 1
            for i in range(25, -1, -1):
                if chars[i] > 0:
                    res += chr(i + 97)
                    chars[i] -= 1
                    remaining -= 1
        return res
