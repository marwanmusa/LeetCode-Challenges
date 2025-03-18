from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0
        for w in words:
            cur = Counter(w)
            ans += len(w)
            for k in cur:
                if not chars.get(k) or cur[k] > chars.get(k):
                    ans -= len(w)
                    break
        return ans