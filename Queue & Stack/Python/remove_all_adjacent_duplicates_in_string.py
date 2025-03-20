class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for a in s:
            if not res: res.append(a)
            else:
                if res[-1] == a: res.pop()
                else: res.append(a)
        return "".join(res)