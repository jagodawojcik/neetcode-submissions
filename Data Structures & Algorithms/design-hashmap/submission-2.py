class MyHashMap:

    def __init__(self):
        self.hash_map = [[] for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        inx = key % len(self.hash_map)
        
        for pair in self.hash_map[inx]:
            if pair[0] == key:
                pair[1] = value
                return

        self.hash_map[inx].append([key, value])

    def get(self, key: int) -> int:
        inx = key % len(self.hash_map)
        
        for pair in self.hash_map[inx]:
            if pair[0] == key:
                return pair[1]

        return -1
        

    def remove(self, key: int) -> None:
        inx = key % len(self.hash_map)
        
        for pair in self.hash_map[inx]:
            if pair[0] == key:
                self.hash_map[inx].remove(pair)
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)