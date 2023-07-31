import re
class Solution:
    """
    Task:
    Given a string s, return the number of segments in the string.

    A segment is defined to be a contiguous sequence of non-space characters.
    """
    def countSegments(self, s: str) -> int:
        return len(re.findall('\S+', s))