from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:
            curWord, count = q.popleft()

            if curWord == endWord:
                return count

            for word in list(wordSet):
                differences = 0

                for i in range(len(curWord)):
                    if curWord[i] != word[i]:
                        differences += 1

                if differences == 1 and word not in visited:
                    visited.add(word)
                    q.append((word, count + 1))

        return 0