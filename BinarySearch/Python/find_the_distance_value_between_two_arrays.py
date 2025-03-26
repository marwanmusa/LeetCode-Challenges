class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res, n = 0, len(arr2)
        for x in arr1:
            l, r, close = 0, n - 1, False
            while (l <= r) :
                mid = l + (r - l) // 2
                cur = arr2[mid]
                if abs(cur - x) <= d:
                    close = True
                    break
                elif cur < x: l = mid + 1
                else: r = mid - 1
            if not close: res += 1
        return res