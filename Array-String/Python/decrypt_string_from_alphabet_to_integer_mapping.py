class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp = {str(i) : chr(i+96) for i in range(1, 27)}
        ans = ''
        for i in range(10, 27):
            mp[str(i)+'#'] = mp[str(i)]
            del mp[str(i)]
        i = 0
        n = len(s)
        while i < n - 2:
            if s[i+2] != '#':
                ans += mp[s[i]]
                i += 1
            else:
                ans += mp[s[i:i+3]]
                i += 3
        if i <= n-1:
            for j in range(i, n):
                ans += mp[s[j]]
        return ans