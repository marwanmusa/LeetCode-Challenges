class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({''.join(codes[ord(x) - ord('a')] for x in w) for w in words})