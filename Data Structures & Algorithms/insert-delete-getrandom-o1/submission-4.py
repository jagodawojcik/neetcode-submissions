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
        
        # Swap last value in the array with the val to remove
        inx_val = self.vals_map[val]
        end_val = self.vals[-1]
        self.vals[inx_val] = end_val

        # Update index
        self.vals_map[end_val] = inx_val
            
        # Remove the val (now it's last value in the arr so it's O(1))
        self.vals.pop()
        # Remove val from vals_map
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