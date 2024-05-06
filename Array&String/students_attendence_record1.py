from collections import Counter

class Solution:
    # brute force
    def checkRecord(self, s: str) -> bool:
        allA = int()
        for a in s:
            if a == 'A': allA += 1        
        return allA < 2 and s.find("LLL") == -1
    
    # shorter version
    def checkRecord(self, s: str) -> bool:
        return Counter(s)['A'] < 2 and s.find("LLL") == -1