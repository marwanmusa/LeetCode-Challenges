class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal: return True
        for i in range(len(s)):
            if s[i+1:] + s[:i+1] == goal:
                return True
        return False
    
    # shorter version
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s 