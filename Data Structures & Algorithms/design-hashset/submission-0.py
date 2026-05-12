class MyHashSet:

    def __init__(self):
        self.stack = []
        

    def add(self, key: int) -> None:
        if not(self.contains(key)):
            self.stack.append(key)
        

    def remove(self, key: int) -> None:
        index = 0
        for i in range(len(self.stack)):
            if self.stack[i] != key:
                self.stack[index] = self.stack[i]
                index += 1
        self.stack = self.stack[0:index]
        

    def contains(self, key: int) -> bool:
        return key in self.stack
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)