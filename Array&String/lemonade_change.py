from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        d = defaultdict(int)
        for bill in bills:
            d[bill] += 1
            if bill == 10:
                if not d.get(5): return False
                d[5] -= 1
            elif bill == 20:
                prem1 = d.get(5) >= 3
                prem2 = (d.get(10) and d.get(5))
                changable = prem1 or prem2
                if not changable: return False
                else:
                    if prem1: d[5] -= 3
                    elif prem2:
                        d[10] -= 1 
                        d[5] -= 1
            else: continue
        return True