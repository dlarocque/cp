class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        # Reverse the list of times, s.t. they are sorted in ascending positions
        for t in time[::-1]:
            # If we encounter a car that is slower than the previous most slowest car,
            # we know that car will never catch up to the previous slowest, so
            # we know that it will be a new fleet
            if t > cur:
                res += 1
                cur = t
        return res
