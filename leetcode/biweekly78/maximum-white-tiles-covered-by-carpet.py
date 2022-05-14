class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        j = cover = res = 0
        for i in range(len(tiles)):
            while j<len(tiles) and tiles[j][1]-tiles[i][0] + 1 <= carpetLen:
                cover += tiles[j][1]-tiles[j][0] + 1
                j += 1
            if j<len(tiles) and tiles[j][0]-tiles[i][0] + 1 <= carpetLen:
                res = max(res, cover + carpetLen-(tiles[j][0]-tiles[i][0]))
            else:
                res = max(res, cover)
            if i!=j:
                cover -= tiles[i][1]-tiles[i][0]+1
        return res
