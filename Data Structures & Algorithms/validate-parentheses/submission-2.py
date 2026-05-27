class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) < 2):
            return False
        stack = []
        for i in range(len(s)):
            temp = s[i]
            if temp == '{' or temp == '[' or temp == '(':
                stack.append(temp)
            else:
                try:
                    check = stack.pop()
                    if (temp == '}' and check != '{') or (temp == ']' and check != '[') or (temp == ')' and check != '('):
                        return False
                except:
                    return False
        return len(stack) == 0