from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5: five += 1
            elif bill == 10 and five: 
                five -= 1; ten += 1
            elif bill == 20 and ten and five:
                five -= 1; ten -= 1
            elif bill == 20 and five >= 3:
                five -= 3
            else: return False
        return True