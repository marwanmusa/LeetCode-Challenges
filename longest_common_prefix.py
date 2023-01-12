class Solution:
    """
    Task:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0] # Setting the 0th element as the prefix

        for i in range(1, len(strs)): # Loop through all elements from index 1 to length -1

            res = str()
            n1 = len(prefix)
            n2 = len(strs[i])

            m = 0
            n = 0
            while m <= n1 - 1 and n <= n2 - 1:
                if (prefix[m] != strs[i][n]):
                    break

                res += prefix[m] # append char prefix at index m if matched
                m += 1
                n += 1

            prefix = res

        return prefix