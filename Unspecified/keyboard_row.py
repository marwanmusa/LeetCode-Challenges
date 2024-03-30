class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = {x : 1 for x in "qwertyuiop"}
        row2 = {x : 2 for x in "asdfghjkl"}
        row3 = {x : 3 for x in "zxcvbnm"}
        row = {**row1, **row2, **row3}
        ans = []
        for w in words:
            check = row[w[0].lower()]
            oneline = True
            for i in range(1, len(w)):
                if row[w[i].lower()] != check:
                    oneline = False
                    break
            if oneline: ans.append(w)
        return ans
                
    # using set methods
    def findWords(self, words):
        return [
            w
            for w in words
            if set(w.lower()).issubset(set("qwertyuiop"))
            or set(w.lower()).issubset(set("asdfghjkl"))
            or set(w.lower()).issubset(set("zxcvbnm"))
        ]