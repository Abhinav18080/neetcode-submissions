class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}      # key -> [value, count]
        self.order = []      # keeps track of recency (left = oldest, right = newest)
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # increment usage counter
        self.cache[key][1] += 1
        # mark as recently used (move to end of order list)
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value + usage count
            self.cache[key][0] = value
            self.cache[key][1] += 1
            # mark as recently used
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.cap:
                # evict least recently used (front of list)
                lru = self.order.pop(0)
                self.cache.pop(lru)
            # insert new key with usage count = 1
            self.cache[key] = [value, 1]
            self.order.append(key)
