import re
from collections import defaultdict, Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower().replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        d = defaultdict(int)
        for w in paragraph.split():
            if w not in banned:
                d[w] += 1
        print(d)
        return max(zip(d.values(), d.keys()))[1]
    
    # shorter
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower().replace('!', ' ').replace('?', ' ').replace("'", ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ')
        d = {k: v for k, v in Counter(paragraph.split()).items() if k not in banned}
        return max(zip(d.values(), d.keys()))[1]
    
    # one liner
    def mostCommonWord(self, p: str, banned: list[str]) -> str:
        return Counter(w for w in re.findall(r'\w+', p.lower()) if w not in set(banned)).most_common(1)[0][0]