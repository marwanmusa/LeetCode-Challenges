class Solution:
    """
    Task:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    """
    # solution 1
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(p, left, right, parens = []):
            if left:            generate(p + '(', left - 1, right)
            if right > left:    generate(p + ')', left, right - 1)
            if not right:       parens += p,
            return parens
        return generate('', n, n)


    # solution 2
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right: 
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))


    # solution 3
    def generateParenthesis(self, n: int, open = 0) -> list[str]:
        """
        Stefan Pochmann:
        Improved version of this. Parameter open tells the number of "already opened" parentheses,
        and I continue the recursion as long as I still have to open parentheses (n > 0) and
        I haven't made a mistake yet (open >= 0).
        """
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)