class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k*2):
            if i + k < len(s):
                s[i:i+k] = s[i:i+k][::-1]
            else:
                s[i:] = s[i:][::-1]
        return ''.join(s)
    
    # most efficient implementation
    def reverseStr(self, s: str, k: int) -> str:
        i, revStr = 0, ""
        while i < len(s):
            revStr += s[i:i+k][::-1]
            revStr += s[i+k:i+(2*k)]
            i += 2*k
        return revStr