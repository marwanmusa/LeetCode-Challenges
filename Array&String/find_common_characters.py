from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        temp = Counter(words[0])
        for i in range(1, len(words)):
            cur = Counter(words[i])
            calc = {w: min(cur[w], temp[w]) for w in (cur.keys() & temp.keys())}
            temp = calc
        ans = []
        for k in temp:
            ans.extend([k] * temp[k])
        return ans