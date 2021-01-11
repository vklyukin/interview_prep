from collections import OrderedDict

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.get(key)
            self.cache.move_to_end(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if (len(self.cache) >= self.capacity) and (key not in self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
