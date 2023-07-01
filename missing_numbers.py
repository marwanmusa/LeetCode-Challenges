from typing import List

class Solution:
    """
    Task:
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    # sum
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)

    # or
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Get sum of complete series(Gaussian formula)
        # and find the difference between sum of given series
        return ((n * (n+1)) // 2 ) - sum(nums)

    # bitwise
    def missingNumber(self, nums: List[int]) -> int:

        result = 0

        for counter, value in enumerate(nums):

            result ^= counter+1 # XOR result with numbers from the complete series
            result ^= value # XOR with the numbers given in num series

        return result

        """
        # Simple break down of above XOR solution

        numsList = [3,0,1] # Missing number is 2

        result = 0

        #XOR result with complete number sequence
        for number in range(len(numsList) + 1 ) : # 0, 1, 2 ,3
                result ^= number

        # Essentially now result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3)

        #XOR result with values in nums
        for num in numsList : # 3,0,1
                result ^= num

        # result = ( 0 ^ 0 ^ 1 ^ 2 ^ 3) ^ ( 3 ^ 0 ^ 1)

        # XOR of same values cancel each other out

        # result = (0) ^ (0 ^ 0)  ^ (1^1) ^ (2) ^ (3^3)
        # result =  0 ^ 0 ^ 0 ^ 2 ^ 0
        # result = 2

        return result # 2
        """

    # shortened bitwise solution
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res