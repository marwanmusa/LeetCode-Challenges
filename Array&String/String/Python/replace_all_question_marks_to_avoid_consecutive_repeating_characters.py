class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        if n == 1 and s == "?": return "a"
        for i in range(n):
            if s[i] == '?':
                for j in range(97, 123):
                    if (i > 0 and s[i-1] == chr(j)) or (i < n - 1 and s[i+1] == chr(j)): continue
                    s[i] = chr(j)
                    break
        return ''.join(s)