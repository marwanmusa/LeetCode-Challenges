class Solution:
    """
    Task:
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
    is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces,
    square brackets are well-formed, etc. Furthermore, you may assume that
    the original data does not contain any digits and that digits are only for those repeat numbers, k.
    For example, there will not be input like 3a or 2[4].

    The test cases are generated so that the length of the output will never exceed 105.
    """
    def decodeString(self, s: str) -> str:
        """
        When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
        push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string