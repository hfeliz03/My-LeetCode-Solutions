class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a hashtable of frequencies { {freq}: [anagrams] }
        hashFreq = {}
        for word in strs:
            anagram  = {}
            anagramKey = tuple(sorted(word))
            if anagramKey not in hashFreq.keys(): hashFreq[anagramKey] = []
            hashFreq[anagramKey].append(word)
        
        return list(hashFreq.values())  