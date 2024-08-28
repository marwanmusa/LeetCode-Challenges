class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        cntn, cntt = 0, 0
        cur = name[0]
        m, n = len(name), len(typed)
        if name[0] != typed[0]: return False
        while i < m:
            cur = name[i]
            if cur != typed[j]: return False
            while j < n and typed[j] == cur:
                cntt += 1
                j += 1
            while i < m and name[i] == cur:
                cntn += 1
                i += 1
            if cntt < cntn or (j < n and i >= m) or (j >= n and i < m): return False
            cntn, cntt = 0, 0
        return True
        