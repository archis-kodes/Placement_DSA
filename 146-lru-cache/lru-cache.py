class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            if key in self.cache:
                self.cache.pop(key)
            else:
                self.cache.pop(list(self.cache)[0])
            self.cache[key] = value
        else:
            if key in self.cache:
                self.cache.pop(key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)