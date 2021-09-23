class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """Return the value associated with the key, or -1 if key is not in the dict"""
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # replace
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # insert
            self.cache[key] = value
            self.size += 1

            if self.size > self.capacity:
                # evict the the LRU kvp
                self.cache.popitem(False) # remove from the start of the ordered dict
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
