class Solution:
    def racecar(self, target: int) -> int:
        steps = 0
        queue = [(0, 1)]
        while queue:
            q = []
            for pos, speed in queue:
                if pos == target:
                    return steps
                
                q.append((pos+speed, speed*2))  # accelerate
                
                if (pos+speed < target and speed < 0) or (pos+speed*2 > target and speed > 0):
                    q.append((pos, -1 if speed >= 0 else 1))  # reverse
                
            steps += 1
            queue = q
