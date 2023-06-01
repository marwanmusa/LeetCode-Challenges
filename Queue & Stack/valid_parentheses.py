class Solution:
    """
    Task:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    """
    def isValid(self, s: str) -> bool:
        left_char = list()
        for char in s:
            if char in ["(","[","{"]:
                left_char.append(char)
            elif char == ")" and len(left_char) != 0 and left_char[-1] == "(":
                left_char.pop()
            elif char == "]" and len(left_char) != 0 and left_char[-1] == "[":
                left_char.pop()
            elif char == "}" and len(left_char) != 0 and left_char[-1] == "{":
                left_char.pop()
            else:
                return False
        return len(left_char) == 0