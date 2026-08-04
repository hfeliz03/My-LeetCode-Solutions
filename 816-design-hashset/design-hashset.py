class MyHashSet:

    def __init__(self):
        self.keys = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.keys.append(key)
        return

    def remove(self, key: int) -> None:
        self.keys.remove(key) if self.contains(key) else None
        return

    def contains(self, key: int) -> bool:
        for k in self.keys:
            if key == k: return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)