class Trie:

    def __init__(self):
        self.bagOfWords = set()

    def insert(self, word: str) -> None:
        self.bagOfWords.add(word)

    def search(self, word: str) -> bool:
        return word in self.bagOfWords

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for word in list(self.bagOfWords):
            if word[:n] == prefix: return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)