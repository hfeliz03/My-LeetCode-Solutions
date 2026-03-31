from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {} #Key-value 
        self.keyStack = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # print(f"get {key=}")
        # print(f"{self.keyStack=}")
        if key in self.lru: 
            self.keyStack.remove(key)
            self.keyStack.append(key)
            return self.lru[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        # print(f"put {key=}")
        # print(f"{self.keyStack=}")
        if key in self.lru: 
            self.keyStack.remove(key)
            self.keyStack.append(key)
            self.lru[key] = value
        else:
            self.keyStack.append(key)
            self.lru[key] = value
            if self.capacity < len(self.lru): #Evict lru
                #print(f"before del {self.lru}")
                del self.lru[self.keyStack.popleft()]
                #print(f"after del {self.lru}")

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)