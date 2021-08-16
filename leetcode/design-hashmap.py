class ListNode:

    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.map = [None] * self.m


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.m
        cur = self.map[i]

        if not cur:
            self.map[i] = ListNode(key, value)
        else:
            while cur:
                if cur.key == key:
                    cur.value = value
                    return
                if not cur.next:
                    cur.next = ListNode(key, value)
                    return

                cur = cur.next


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.m
        cur = self.map[i]

        if not cur:
            return -1
        else:
            while cur:
                if cur.key == key:
                    return cur.value
                cur = cur.next

            # reached then end of the list without finding the key
            return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.m
        prev = cur = self.map[i]

        if not cur:
            return
        if cur.key == key:
            self.map[i] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
