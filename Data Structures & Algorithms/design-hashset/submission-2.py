class MyHashSet:
 # since there are million of keys we could just use boolean array
    def __init__(self):
        self.hash_set = [False for i in range(1000000)]
        
    def add(self, key: int) -> None:
        self.hash_set[key] = True

    def remove(self, key: int) -> None:
        self.hash_set[key] = False
        
        
    def contains(self, key: int) -> bool:
        return self.hash_set[key]
     


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)