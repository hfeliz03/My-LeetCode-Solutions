class MyHashMap:
    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.hashmap.append((key, value))
        
        return 

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.hashmap):
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        value = self.get(key)
        if value != -1:
            self.hashmap.remove((key,value))
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)