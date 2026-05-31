class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if len(stack) == 0:
                    return False
                lastElement = stack.pop()
                if (i == ')' and lastElement == '(') or (i == '}' and lastElement == '{') or (i == ']' and lastElement == '['):
                    continue
                else:
                    return False
        return len(stack) == 0