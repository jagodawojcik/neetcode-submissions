class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.pairs = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # if key exists: return its val, remove and append to top
        # if key doesn't exit: return -1

        if key in self.pairs:
            self.cache.remove(key) # O(n)
            self.cache.append(key)
            return self.pairs[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update it's value, remove and append to top
        # if doesn't, check, capacity, then either append or remove LRU val then append

        if key in self.pairs:
            self.pairs[key] = value
            self.cache.remove(key) # O(n)
            self.cache.append(key)
            return
        
        if len(self.cache) < self.capacity:
            self.cache.append(key)
            self.pairs[key] = value
            return

        
        key_rem = self.cache.pop(0) # O(n)
        del self.pairs[key_rem]
        self.cache.append(key)
        self.pairs[key] = value
        return


        
