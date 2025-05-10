class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        cnt, idx = 0, 0
        while cnt < n + 1:
            if idx > n-1 or cnt > n - idx: return -1
            if cnt <= nums[idx] and cnt == n - idx:
                return cnt
            elif cnt > nums[idx]:
                idx += 1
            else:
                cnt += 1
        return -1

    # Binary Search approach
    def specialArrayBinarySearch(self, nums: list[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            cnt = sum(num >= mid for num in nums)
            if cnt == mid:
                return mid
            elif cnt < mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1