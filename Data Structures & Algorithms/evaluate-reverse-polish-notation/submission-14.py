class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for token in tokens:
            if token not in "+-*/":
                operands.append(int(token))
            else:
                num1 = operands.pop()
                num2 = operands.pop()

                if token == "+":
                    operands.append(num2 + num1)
                elif token == "-":
                    operands.append(num2-num1)
                elif token == "*":
                    operands.append(num2*num1)
                elif token == "/":
                    operands.append(int(num2/num1))
        
        return operands.pop()