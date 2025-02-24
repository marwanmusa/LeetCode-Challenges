class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                image[i][j] = abs(image[i][j] - 1)
        return image