class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [item for pair in zip(nums[:n], nums[n:]) for item in pair]
