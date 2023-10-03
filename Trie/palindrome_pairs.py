"""
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:
    - 0 <= i, j < words.length,
    - i != j, and
    - words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.
"""


class Solution:
    """
    check each word for prefixes (and suffixes) that are themselves palindromes.
    If you find a prefix that is a valid palindrome, then the suffix reversed can be paired
    with the wordin order to make a palindrome.
    
    It's better explained with an example.
    words = ["bot", "t", "to"]
    """
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals
    
    # Hashmap
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        # keep a hashmap of word to its index
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        res = set()
        for i, word in enumerate(words):
            if not word:
                # we don't process empty string by itself
                continue
            
            # generate all possible LHS that would form
            # a palindrome with current word
            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((idx_map[target], i))
                    
            # generate all possible RHS that would form
            # a palindrome with current word
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    res.add((i, idx_map[target]))
                    
            # check if current word is already a palindrome and
            # if we have an empty string in our map
            if word == word[::-1] and "" in idx_map:
                idx = idx_map[""]
                res.add((i, idx))
                res.add((idx, i))

        return list(res)
    
    # Map Matching
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        wmap, ans = {}, []
        for i in range(len(words)):
            wmap[words[i]] = i
        for i in range(len(words)):
            if words[i] == "":
                for j in range(len(words)):
                    w = words[j]
                    if self.isPal(w, 0, len(w)-1) and j != i:
                        ans.append([i, j])
                        ans.append([j, i])
                continue
            bw = words[i][::-1]
            if bw in wmap:
                res = wmap[bw]
                if res != i: ans.append([i, res])
            for j in range(1, len(bw)):
                if bw[j:] in wmap and self.isPal(bw, 0, j - 1):
                    ans.append([i, wmap[bw[j:]]])
                if bw[:j] in wmap and self.isPal(bw, j, len(bw)-1):
                    ans.append([wmap[bw[:j]], i])
        return ans

    def isPal(self, word: str, i: int, j: int) -> bool:
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True