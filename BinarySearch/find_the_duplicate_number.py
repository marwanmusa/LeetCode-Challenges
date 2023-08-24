from typing import List

class Solution:
    """
    Task:
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
    """

    # Approach 1: Sort
    """
    Note: This approach modifies individual elements and does not use constant space,
    and hence does not meet the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    
    # Approach 2: Set
    """
    Note: This approach does not use constant space, and hence does not meet the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
    
    # Approach 3: Negative Marking
    """
    Note: This approach temporarily modifies individual elements and thus does not satisfy the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # mark all negative numbers as visited (negative marking technique)
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return duplicate
    
    # Approach 4.1: Array as HashMap (Recursion)
    """
    Note: Approaches 4.1 and 4.2 modify individual elements, and hence do not meet the problem constraints.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        def store(nums: List[int], cur: int) -> int:
            if cur == nums[cur]:
                return cur
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)
        return store(nums, 0)

    # Approach 4.1: Array as HashMap (Iterative)
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]

    # Approach 5: Binary Search
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        while l <= r:
            cur = l + (r-l)//2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                r = cur-1
            else:
                l = cur+1
        return duplicate
    
    # Approach 6: Sum of Set Bits
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums)-1
        bits = n.bit_length()
        for bit in range(bits):
            mask = 1 << bit
            base_count = 0
            nums_count = 0
            for i in range(n+1):
                # if bit is set in number (i) then add 1 to base count
                if i & mask:
                    base_count += 1
                
                # if bit is set in nums[i] then add 1 to nums_count
                if nums[i] & mask:
                    nums_count += 1

            # if the current bit is more frequently set in nums than it is in
            # the range (1, 2, ..., n) the it must also be set in the duplicate number.
            if nums_count - base_count > 0:
                duplicate |= mask
        return duplicate
