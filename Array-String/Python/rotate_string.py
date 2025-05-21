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
    

    # kmp algo
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if len(A) == 0: return True
        
        # capture length of strings
        # then make both strings 1 indexed
        N = len(A)
        A = " " + A + A
        B = " " + B
        
        # calculate pi table, it captures the length of the
		# longest prefix that is also the suffix
        pi = [0] * (N+1)
        left, pi[0] = -1, -1
        for right in range(1, N+1):
            while left >= 0 and B[left + 1] != B[right]:
                left = pi[left]
            left += 1
            pi[right] = left
        
        # do matching
        j = 0
        for i in range(1, (2*N)+1):
            while j >= 0 and B[j+1] != A[i]:
                j = pi[j]
            j += 1
            if j == N: return True
        
        return False