class Solution:
    """
    Task:
    Given two binary strings a and b, return their sum as a binary string.
    """
    def addBinary(self, a: str, b: str) -> str:
        n = list(str(int(a) + int(b)))
        idx = len(n) - 1 # we will add constraints for idx == 0
        while idx > 0:
            if int(n[idx]) >= 2:
                n[idx - 1] = str(int(n[idx - 1]) + int(n[idx])//2)
                n[idx] = str(int(n[idx])%2)
            idx -= 1
        if n[0] == "2": n[0] = "10"
        elif n[0] == "3": n[0] = "11"
        return "".join(n)