class Solution:
    def reformatDate(self, date: str) -> str:
        M = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
             "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        sd, cur, ans, delim, sep = [], "", "", ' ', '-'
        for w in date:
            if w == delim:
                sd.append(cur)
                cur = ""
            else: cur += w
        ans += cur + sep + M[sd[1]] + sep
        ans += sd[0][:2] if len(sd[0]) == 4 else '0' + sd[0][0]
        return ans