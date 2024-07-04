class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = collections.Counter(paragraph.lower().split()).most_common()
        print(cnt)
        if not banned:
            return cnt[0][1]
        for w in cnt:
            if w[0] not in banned: return w[0] 