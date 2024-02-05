from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = 0
        l = 0
        r = len(people) - 1
        people.sort()
        while l < r:
            num = people[l] + people[r] 
            if num <= limit:
                counter += 1
                l += 1
                r -= 1
            elif num > limit:
                counter += 1
                r -= 1
        if l == r:
            counter += 1
        return counter


    # More efficient way
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people)-1
        res = 0
        while light <= heavy:
            remain = limit - people[heavy]
            heavy -= 1
            res += 1
            if light <= heavy and remain >= people[light]:
                light += 1
        return res