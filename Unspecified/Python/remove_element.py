from typing import List

class Solution:
    """
    Task:
    Given an integer array nums and an integer val, remove all occurrences of
    val in nums in-place. The relative order of the elements may be changed.

    Since it is impossible to change the length of the array in some languages,
    you must instead have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates,
    then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying
    the input array in-place with O(1) extra memory.
    """
    # Store all val idx in nums, then remove all val by idx and -1 the idx each loop
    def removeElement(self, nums: List[int], val: int) -> int:
        val_idx = []
        k = len(nums) - len(val_idx)
        for i in range(len(nums)):
            if nums[i] == val: val_idx.append(i)
        offset = 0
        for j in val_idx:
            nums.pop(offset + j)
            offset -= 1
        return k

    # Swap all val to the end of the array
    def removeElement(self, nums: List[int], val: int) -> int:
        writeIdx = 0
        for readIdx in range(0, len(nums)):
            if nums[readIdx] != val:
                nums[readIdx], nums[writeIdx] = nums[writeIdx], nums[readIdx]
                writeIdx += 1
        return writeIdx

    # Use python built-in functions
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = list(filter((val).__ne__, nums))
        return len(nums)