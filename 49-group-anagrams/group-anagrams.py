class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a hashtable of frequencies { {freq}: [anagrams] }
        hashFreq = {}
        for word in strs:
            anagram  = {}
            for letter in word :
                anagram[letter] = anagram.get(letter, 0 ) + 1
            
            anagramKey = tuple(sorted(anagram.items()))
            if anagramKey not in hashFreq.keys(): hashFreq[anagramKey] = []
            hashFreq[anagramKey].append(word)
        
        return list(hashFreq.values())  