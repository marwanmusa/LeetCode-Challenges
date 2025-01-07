class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return [m[1] for m in sorted([[sum(matx), i] for i, matx in enumerate(mat)])[:k]]
