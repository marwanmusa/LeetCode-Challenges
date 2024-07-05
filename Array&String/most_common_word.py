from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower().replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        d = defaultdict(int)
        for w in paragraph.split():
            if w not in banned:
                d[w] += 1
        print(d)
        return max(zip(d.values(), d.keys()))[1]