from typing import List

class Solution:
    """
    Task:
    Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

    Return a list of all possible strings we could create. Return the output in any order.
    """
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]

        for c in s:
            tmp=[]
            if c.isalpha():
                for o in output:
                    tmp.append(o+c.lower())
                    tmp.append(o+c.upper())
            else:
                for o in output:
                    tmp.append(o+c)
            output = tmp

        return output