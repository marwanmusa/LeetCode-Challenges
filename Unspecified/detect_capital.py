import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up = re.findall("[A-Z]", word)
        low = re.findall("[a-z]", word)
        return True if (len(up) == 1 and up[0] == word[0]) or (not up or not low) else False
            