class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        r, c = len(img), len(img[0])
        ans = []
        for i in range(r):
            curi = []
            for j in range(c):
                cur, n = img[i][j], 1
                for pos in [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                            [0, 1], [1, -1], [1, 0], [1, 1]]:
                    if 0 <= i+pos[0] < r and 0 <= j+pos[1] < c:
                        cur += img[i+a][j+b]
                        n += 1
                curi.append(cur//n)
            ans.append(curi)
        return ans