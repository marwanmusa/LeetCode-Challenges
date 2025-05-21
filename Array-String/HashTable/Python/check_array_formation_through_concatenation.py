class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        remain, idxs = len(arr), {v: i for i, v in enumerate(arr)}
        for piece in pieces:
            piece_width = len(piece)
            if piece[0] not in idxs: return False

            prev = idxs[piece[0]]
            remain -= 1

            for j in range(1, piece_width):
                if (piece[j] not in idxs) or (idxs.get(piece[j]) != prev + 1):
                    return False
                prev += 1
                remain -= 1
        return remain == 0
