class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        zeros = k
        for x in nums:
            if x == 1:
                if zeros < k:
                    return False
                zeros = 0  # Reset count of zeros
            else:
                zeros += 1  # Count zeros between 1s

        return True