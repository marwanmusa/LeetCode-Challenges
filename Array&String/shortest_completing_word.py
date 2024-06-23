import collections
class Solution:
    """
    Task:
    Given a string licensePlate and an array of strings words, find the shortest completing word in words.

    A completing word is a word that contains all the letters in licensePlate.
    Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
    If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

    For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
    Possible completing words are "abccdef", "caaacab", and "cbca".

    Return the shortest completing word in words. It is guaranteed an answer exists.
    If there are multiple shortest completing words, return the first one that occurs in words.


    """
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        licensePlate = licensePlate.lower()
        lp = collections.Counter([x for x in licensePlate if x.isalpha()])
        
        def check(lp, word):
            for w in lp:
                print(word, w)
                if lp[w] > word.count(w): return False
            return True
        
        cur = ""
        for i, w in enumerate(words):
            if not cur:
                if check(lp, w):
                    cur = w
            else:
                if check(lp, w) and len(cur) > len(w):
                    cur = w
        return cur
    
    # shorter version
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        lp = collections.Counter([x for x in licensePlate.lower() if x.isalpha()])
        return min([w for w in words if collections.Counter(w) & lp == lp], key=len)