class Solution:
    def selfDividingNumbers(self, l: int, r: int) -> List[int]:
        def check(n):
            a = n
            while n > 0:
                rem = n%10
                if rem == 0 or a % rem != 0: return False
                n //= 10
            return True
        return [i for i in range(l, r+1) if check(i)]

    # one-line
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right+1) if all(i and (x % i == 0) for i in map(int, str(x)))]
