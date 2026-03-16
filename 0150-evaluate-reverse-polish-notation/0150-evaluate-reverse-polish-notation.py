class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                op1 = stack.pop()
                op2 = stack.pop()
                if token == "+":
                    stack.append(op1+op2)
                elif token == "-":
                    stack.append(op2-op1)
                elif token == "*":
                    stack.append(op1*op2)
                elif token == "/":
                    
                    stack.append(math.trunc(op2/op1))
            else:
                stack.append(int(token))
            print(stack)

        return stack[0]