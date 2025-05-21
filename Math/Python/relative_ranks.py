class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        arr = sorted(score, reverse = True)
        map_sc = {arr[i] : i for i in range(len(arr))}
        high_rank = {0 : "Gold Medal", 1 : "Silver Medal", 2 : "Bronze Medal"}
        return [str(map_sc[num] + 1) if map_sc[num]>2 else high_rank[map_sc[num]] for num in score]
    
    # add another approach
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort = sorted(score)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i+1) for i in range(3, len(score))]
        return map(dict(zip(sort, rank)).get, score)
