class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        res = ""
        n = len(s)
        remainder = n % k
        for i in range(remainder, n, k):
            res += '-' + s[i:i+k]
        if remainder > 0:
            return s[:remainder] + res
        else:
            return res[1:]

    # shorter solution
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i+k] for i in range(0, len(s), k))[::-1]
    
    # without reversing the string
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        if k > len(s) : return s
        res = '-'.join(s[i:i+k] for i in range(len(s) % k, len(s), k))
        return s[:len(s) % k] + '-' +  res if len(s) % k > 0 else res
