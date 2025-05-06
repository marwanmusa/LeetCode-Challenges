class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            # All spaces go after the single word
            return words[0] + ' ' * spaces
        partition, extra = divmod(spaces, len(words) - 1)
        return (' ' * partition).join(words) + ' ' * extra