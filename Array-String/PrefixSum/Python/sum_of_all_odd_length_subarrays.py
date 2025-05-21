from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        total_sum = 0
        for length in range(1, n + 1, 2):
            for start in range(n - length + 1):
                total_sum += prefix_sum[start + length] - prefix_sum[start]

        return total_sum

    # O(n) solution
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        for i in range(n):
            total_sum += arr[i] * ((i + 1) * (n - i + 1) + 1) // 2
        return total_sum