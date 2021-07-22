class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            # try to insert a flower
            if flowerbed[i] == 0:
                # check if it is possible to insert a flower
                available = True
                if i > 0:
                    if flowerbed[i-1] != 0:
                        available = False
                if i < len(flowerbed)-1:
                    if flowerbed[i+1] != 0:
                        available = False
                if available == True:
                    flowerbed[i] = 1
                    placed += 1
                    if placed == n:
                        return True
        return False
