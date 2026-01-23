class Solution:
    letters = {
            "2": ["a","b","c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }

    output = {""}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list(self.output)
        
        curOutput = self.output.copy()
        for i, letter in enumerate(self.letters[digits[0]]):
            for prevStr in self.output:
                curOutput.add(prevStr + letter)

        self.output = curOutput - self.output

        return self.letterCombinations(digits[1:])
        
