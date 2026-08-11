class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.vals_map = {} # val: index
        

    def insert(self, val: int) -> bool:
        if val not in self.vals_map:
            self.vals.append(val)
            self.vals_map[val] = len(self.vals) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.vals_map:
            return False

        index = self.vals_map[val]
        last_val = self.vals[-1]

        # Move last element into the removed element's position
        self.vals[index] = last_val
        self.vals_map[last_val] = index

        # Remove last element
        self.vals.pop()
        del self.vals_map[val]

        return True
        

    def getRandom(self) -> int:
        inx = random.randint(0, len(self.vals) - 1)
        return self.vals[inx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()