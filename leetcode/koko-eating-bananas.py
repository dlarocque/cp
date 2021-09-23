class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hour(speed):
            hour = 0
            for n in piles:
                hour+=math.ceil(n/speed)
            return hour

        max_speed = -float(inf)

        for n in piles:
            max_speed = max(max_speed, n)

        res = max_speed
        min_speed = 1
        while min_speed<=max_speed:
            mid_speed = min_speed+(max_speed-min_speed)//2
            hour = calculate_hour(mid_speed)
            if hour<=h:
                res = min(res, mid_speed)
                max_speed = mid_speed-1
            else:
                min_speed = mid_speed+1
        return res
