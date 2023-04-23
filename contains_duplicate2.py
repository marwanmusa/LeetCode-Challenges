class Solution:
    """
    Task:
    Given an integer array nums and an integer k,
    return true if there are two distinct indices i and j in the array
    such that nums[i] == nums[j] and abs(i - j) <= k.
    """
    # Method 1 using set
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = set()
        for i in range(len(nums)):
            if nums[i] in l:
                return True
            l.add(nums[i])
            if i >= k:
                l.remove(nums[i-k])
        return False

    # Method 2 using dictionary
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hm = {}
        for i, n in enumerate(nums):
            if n in hm and abs(hm[n]-i)<=k:
                return True
            hm[n] = i
        return False