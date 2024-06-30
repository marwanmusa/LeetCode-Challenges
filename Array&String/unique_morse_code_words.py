class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = {chr(i+97): codes[i] for i in range(len(codes))}
        return len(set(''.join([morse[x] for x in w]) for w in words))