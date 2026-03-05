class Solution:
    def isValid(self, s: str) -> bool:
      # (((()))))]]]
      # If stack.peek != curr element closing parenthesis: return false 
      # If stack is still populated at the end, return false
        if len(s) %2 != 0 : return False
        PARENS = {"(": ")", "[":"]", "{":"}"}
        stack = []
        for char in s:

            if char in PARENS.keys():
                stack.append(char)
            else:
                if len(stack) == 0: return False
                lastElem = stack[-1]
                if PARENS[lastElem] == char:
                    stack.pop()
                else: return False

        return True if len(stack) == 0 else False
                