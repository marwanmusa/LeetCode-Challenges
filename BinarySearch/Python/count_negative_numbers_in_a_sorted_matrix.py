class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        res = 0
        def countNeg(row):
            i, j, neg = 0, len(row) - 1, 0
            if len(row) == 1:
                return row[0] < 0
            while i < j:
                if row[i] >= 0 and row[j] >= 0:
                    break
                elif row[i] < 0 and row[j] < 0:
                    neg += (j - i + 1)
                    break
                elif row[i] < 0 and row[j] >= 0:
                    neg += 1
                    i += 1
                else:
                    neg += 1
                    j -= 1
            return neg
        for row in grid:
            res += countNeg(row)
        return res