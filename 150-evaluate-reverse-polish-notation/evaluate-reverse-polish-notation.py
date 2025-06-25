class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for i in tokens:
            match i:
                case '+':
                    values.append(values.pop() + values.pop())
                case '-':
                    subtrahend, minuend  = values.pop(), values.pop()
                    values.append(minuend - subtrahend)
                case '*':
                    values.append(values.pop() * values.pop())
                case '/':
                    divisor, dividend = values.pop(), values.pop()
                    values.append( math.trunc(dividend / divisor))
                case _:
                    values.append(int(i))
            
        return values.pop()