class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        temp, rank, cnt, ans = sorted(arr), {}, 1, []
        for x in temp:
            if rank.get(x): continue
            rank[x] = cnt
            cnt += 1

        for x in arr: ans.append(rank[x])
        return ans

    # shorter
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        temp = sorted(set(arr))
        rank = {value : i+1 for i, value in enumerate(temp)}
        return [rank[x] for x in arr]