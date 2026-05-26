class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerCase, upperCase = set(), set()
        for letter in word:
            if ord(letter) >= 95: 
                lowerCase.add(letter)
            else: 
                letter = letter.lower()
                upperCase.add(letter)
                
        print(upperCase)
        print(lowerCase)
        return len(lowerCase & upperCase)