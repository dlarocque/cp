class StockPrice:
    
    def __init__(self):
        self.dict = {}
        self.max_timestamp = []
        self.max_price = []
        self.min_price = []

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.max_timestamp, -timestamp)
        heapq.heappush(self.max_price, (-price, timestamp))
        heapq.heappush(self.min_price, (price, timestamp))
        self.dict[timestamp] = price    

    def current(self) -> int:
        # return the price of the latest timestamp
        return self.dict[-self.max_timestamp[0]]

    def minimum(self) -> int:
        # pop while the price is out of date with the current price
        while self.dict[self.min_price[0][1]] != self.min_price[0][0]:
            heapq.heappop(self.min_price)
        
        return self.min_price[0][0]

    def maximum(self) -> int:
        while self.dict[self.max_price[0][1]] != -self.max_price[0][0]:
            heapq.heappop(self.max_price)
        
        return -self.max_price[0][0]        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
