from collections import defaultdict, Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s): return True
        diff = []
        for a,b in zip(s, goal):
            if a != b:
                diff.append((a,b))
                if len(diff) > 2: return False
        return len(diff) == 2 and diff[0] == diff[1][::-1]
    

    # 2 solution
    def buddyStrings_v2(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal:
            return len(set(s)) < len(s)
        I, J = None, None
        for i, (a, b) in enumerate(zip(s, goal)):
            if a != b:
                if I is None:
                    I = i
                elif J is None:
                    J = i
                else:
                    return False
        if J is None: return False
        return s[I] == goal[J] and s[J] == goal[I]
