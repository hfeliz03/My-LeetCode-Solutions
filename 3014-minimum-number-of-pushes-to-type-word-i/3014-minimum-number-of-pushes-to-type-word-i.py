class Solution:
    def minimumPushes(self, word: str) -> int:
        wordFreq = Counter(word)
        if len(wordFreq) < 9: return len(wordFreq)
        #sort by largest count such that those go first
        countDict = defaultdict(list)
        for key, val in wordFreq.items():
            countDict[val].append(key)
        print(countDict)
        keysSorted = sorted(countDict.keys(), reverse = True)
        
        res = 0
        presses = 1
        visited = set()
        for key in keysSorted:
            while countDict[key]:
                visited.add(countDict[key].pop())
                res += presses*key
                if (len(visited)) % 8 == 0: presses += 1
        return res