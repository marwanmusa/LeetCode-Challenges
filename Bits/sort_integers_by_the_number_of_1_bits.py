class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return [res[1] for res in sorted([[x.bit_count(), x] for x in arr])]

    # shorter version
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key = lambda x: (x.bit_count(), x))

    # using the original array
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key = lambda x: (x.bit_count(), x))
        return arr