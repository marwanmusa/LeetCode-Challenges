class Solution:
    """
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
    and with the smallest space complexity possible.
    """
    # Using built-in
    def sortArray(self, nums: list[int]) -> list[int]:
        return sorted(nums)

    # Using merge sort
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        mid = int(len(nums)/2)
        l_nums = self.sortArray(nums[:mid])
        r_nums = self.sortArray(nums[mid:])
        
        def merge(l:list, r:list) -> list:
            ptr_l = ptr_r = 0
            ans = []
            while ptr_l < len(l) and ptr_r < len(r):
                if l[ptr_l] < r[ptr_r]:
                    ans.append(l[ptr_l])
                    ptr_l += 1
                else:
                    ans.append(r[ptr_r])
                    ptr_r += 1
            ans.extend(l[ptr_l:])
            ans.extend(r[ptr_r:])
            return ans
        
        return merge(l_nums, r_nums)
    
    # Merge-sort 2
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]

            self.sortArray(l)
            self.sortArray(r)

            i = j = k = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    nums[k] = l[i]
                    i += 1
                else:
                    nums[k] = r[j]
                    j += 1
                k += 1
            
            while i < len(l):
                nums[k] = l[i]
                i += 1
                k += 1
            while j < len(j):
                nums[k] = r[j]
                j += 1
                k += 1
        return nums

    # Buble-sort TLE
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
    # Insertion-sort TLE
    def sortArray(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i-1
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

    # Quick-sort TLE
    def sortArray(self, nums: list[int]) -> list[int]:
        def helper(head, tail):
            if head >= tail: return None
            l, r = head, tail
            m = l + (r-l) // 2
            mid = nums[m]
            while r >= l:
                while r >= l and nums[l] < mid: l += 1
                while r >= l and nums[r] > mid: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums
    
    # Heap-sort
    def sortArray(self, nums: list[int]) -> list[int]:
        def heapify(nums, n, i):
            l = 2*i+1
            r = 2*i+2

            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l

            if r < n and nums[largest] > nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n//2+1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)