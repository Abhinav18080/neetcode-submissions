class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openbracket, closedbracket):
            if(openbracket == closedbracket == n):
                res.append("".join(stack))
                return
            
            if openbracket < n:
                stack.append("(")
                backtrack(openbracket+1, closedbracket)
                stack.pop()

            if closedbracket < openbracket:
                stack.append(")")
                backtrack(openbracket, closedbracket + 1)
                stack.pop()
        
        backtrack(0,0)
        return res