class Solution:
    def isNum(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        operand = []

        for i in tokens:
            if self.isNum(i) == True:
                operand.append(int(i))
            else:
                num1 = operand.pop()
                num2 = operand.pop()
                if i == '+':
                    res = num1 + num2 
                    operand.append(res)
                elif i == '-':
                    res = num2 - num1
                    operand.append(res)
                elif i == '*':
                    res = num1 * num2
                    operand.append(res)
                else:
                    res = num2 / num1
                    operand.append(int(res))
        return int(operand.pop())