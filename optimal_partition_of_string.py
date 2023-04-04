class Solution:
    """
    Task:
    Given a string s, partition the string into one or more substrings such that
    the characters in each substring are unique. That is, no letter appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.
    """
    def partitionString(self, s: str) -> int:
        count = 0
        partition = set()
        for char in s:
            if char in partition:
                count += 1
                partition.clear()
            partition.add(char)
        return count + 1