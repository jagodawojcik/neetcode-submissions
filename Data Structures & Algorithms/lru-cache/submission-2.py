class Node:
    def __init__(self, val, key, next = None, prev = None):
        self.val, self.key, self.next, self.prev = val, key, next, prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, self.left)
        self.left.next = self.right
        self.cache = {} # key, Node

        # (LRU) left_node -> cache_n1 -> cache_n2 -> right_node (Most Rec Used)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def append(self, node):
        tmp = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = tmp


    def get(self, key: int) -> int:
        # if key exists: return its val, remove node and append to top
        # if key doesn't exit: return -1

        if key in self.cache:
            self.remove(self.cache[key])# O(n)
            self.append(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update it's value, remove and append to top
        # if doesn't, check, capacity, then either append or remove LRU val then append
        if key in self.cache:
            self.remove(self.cache[key]) # O(n)
            self.cache[key].val = value
            self.append(self.cache[key])
            return
        
        if len(self.cache) < self.capacity:
            self.cache[key] = Node(value, key)
            self.append(self.cache[key])
            return

        
        key_rem = self.left.next.key
        self.remove(self.cache[key_rem])
        del self.cache[key_rem]
        self.cache[key] = Node(value, key)
        self.append(self.cache[key])
        return


        
