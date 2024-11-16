class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr1 = sorted(arr1)
        idx_map = {v : i+1 for i,v in enumerate(arr2)}
        idx_map = {v : len(arr1) if not idx_map.get(v) else idx_map[v]-1 for i,v in enumerate(arr1)}
        return sorted(arr1, key=idx_map.get)