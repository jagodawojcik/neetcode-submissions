class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for i in range(10000)]
        
    def add(self, key: int) -> None:
        index = key % len(self.hash_set)

        for k in self.hash_set[index]:
            if k == key:
                return
        self.hash_set[index].append(key)



    def remove(self, key: int) -> None:
        index = key % len(self.hash_set)

        if key in self.hash_set[index]:        
            self.hash_set[index].remove(key)

        
        
    def contains(self, key: int) -> bool:
        return key in self.hash_set[key % len(self.hash_set)]
     

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)