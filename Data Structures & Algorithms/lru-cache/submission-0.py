class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self,node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = next_node.prev = node
        node.next = next_node
        node.prev = prev_node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next          # save node first
            self.remove(lru)              # unlink it
            del self.cache[lru.key]  
        
