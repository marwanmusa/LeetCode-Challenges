class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs[0])
        idxs = set(range(len(strs[0])))
        cur = strs[0]
        for s in strs[1:]:
            stack = set()
            for idx in idxs:
                if s[idx] < cur[idx]: stack.add(idx)
            idxs -= stack
            cur = s
        return n - len(idxs)

    # shorter
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count