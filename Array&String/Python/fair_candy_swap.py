class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        suma = sum(aliceSizes)
        sumb = sum(bobSizes)
        diff = (suma - sumb) / 2
        aliceSizes = set(aliceSizes)
        for el in set(bobSizes):
            if el + diff in aliceSizes:
                return [el + diff, el]
