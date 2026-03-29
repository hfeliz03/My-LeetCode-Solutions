class WordDictionary:

    def __init__(self):
        # b: {a:{ d:{}, c{}}, l:{ a{}, }}
        self.words = {}

    def addWord(self, word: str) -> None:
        cur = self.words
        for ch in word:
            cur = cur.setdefault(ch, {})
        cur["*"] = True
            
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return "*" in node

            c = word[i]

            if c != ".":
                if c not in node:
                    return False
                return dfs(i + 1, node[c])
            else:
                for child in node:
                    if child != "*" and dfs(i + 1, node[child]):
                        return True
                return False

        return dfs(0, self.words)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)