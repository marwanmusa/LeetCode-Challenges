class Solution:
    """
    In English, we have a concept called root, which can be followed by some other word
    to form another longer word - let's call this word successor. 
    For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

    Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
    replace all the successors in the sentence with the root forming it. 
    If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

    Return the sentence after the replacement.
    """
    # Approach 1: Prefix Hash
    # For each word in the sentence, we'll look at successive prefixes and see if we saw them before
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word
        
        return " ".join(map(replace, sentence.split()))