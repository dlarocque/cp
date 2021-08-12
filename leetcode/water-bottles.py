class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty, drank = 0, 0

        while numBottles > 0:
            # drink all of the water bottles
            drank += numBottles
            empty += numBottles

            # exchange the empty bottles for full ones
            numBottles = empty // numExchange
            empty %= numExchange

        return drank
