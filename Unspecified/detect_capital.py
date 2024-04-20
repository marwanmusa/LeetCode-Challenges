import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up = re.findall("[A-Z]", word)
        low = re.findall("[a-z]", word)
        if len(up) == 1 and up[0] == word[0]:
            return True
        if not up or not low:
            return True
        return False
            