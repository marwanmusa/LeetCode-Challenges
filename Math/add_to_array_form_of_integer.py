from collections import deque

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n, numint, idx = len(num) - 1, 0, 0
        numint = 0
        while n >= 0:
            numint += ((10 ** n) * num[idx])
            idx += 1
            n -= 1
        numint += k

        ans = deque()
        while numint > 0:
            ans.appendleft(numint % 10)
            numint //= 10
        return ans

    # more-efficient
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1
        while k > 0:
            if i >= 0:
                k = num[i]
                num[i] = k % 10
                i -= 1
            else:
                num.insert(0, k % 10)
            k //= 10
        return num