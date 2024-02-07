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