class Solution:
    """
    Task:
    Assume you are an awesome parent and want to give your children some cookies.
    But, you should give each child at most one cookie.

    Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
    and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.
    Your goal is to maximize the number of your content children and output the maximum number.
    """
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if not s: return 0
        g.sort()
        s.sort()
        res = 0
        childidx = len(g) - 1 
        cookieidx = len(s) - 1
        while childidx >= 0 and cookieidx >= 0:
            if g[childidx] <= s[cookieidx]:
                res += 1
                cookieidx -= 1
            childidx -= 1
        return res
    

    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if not s: return 0
        g.sort()
        s.sort()
        cnt, j, l = 0, 0, len(s)
        for i in range(l):
            if s[i] >= g[j]:
                j += 1
                count += 1
            if j >= len(g):
                break
        return cnt
    

    def getContentChildren(self, g: list[int], s: list[int]) -> int:
        stack = sorted(g, reverse=True)
        s = sorted(s)
        for i in range(len(s)):
            if stack and stack[-1] <= s[i]:
                stack.pop()
        return len(g) - len(stack)
    

    def getContentChildren(self, g: list[int], s: list[int]) -> int:
        if not s: return 0
        g.sort()
        s.sort()
        cnt, j = 0, len(s)-1
        for i in range(len(g)-1, -1, -1):
            if j >= 0 and s[j] >= g[i]:
                cnt += 1
                j -= 1
        return cnt