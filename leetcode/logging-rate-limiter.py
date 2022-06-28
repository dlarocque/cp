from collections import defaultdict
class Logger:

    def __init__(self):
        self.timestamps = defaultdict(lambda: -10)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        min_time = self.timestamps[message] + 10
        if timestamp >= min_time:
            self.timestamps[message] = timestamp
            return True
        else:
            return False
