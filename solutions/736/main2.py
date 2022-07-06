from collections import deque 
class Solution:
    def parseExp(self, expression):
        # similar to leetcode 385
        stack = deque()
        temp_exp = ""
        for ch in expression:
            if ch == "(":
                stack.append([])
            elif ch in [" ", ")"]:
                if len(temp_exp) > 0:  
                    stack[-1].append(temp_exp)
                    temp_exp = ""
                if ch == ")" and len(stack) > 1: 
                    prev = stack.pop()
                    stack[-1].append(prev)
            else: 
                temp_exp += ch 
        result = stack[0] if len(stack) > 0 else [temp_exp] 
        return result 
    def letExp(self, expression, scope): 
        scope[expression[0]] = self.calExp(expression[1], scope)
        return scope 
    def addExp(self, expression, scope): 
        return self.calExp(expression[0], scope) + self.calExp(expression[1], scope)
    def multExp(self, expression, scope): 
        return self.calExp(expression[0], scope) * self.calExp(expression[1], scope)
    def calExp(self, expression, scope):
        # base case, after let expression  
        if type(expression) != list:
            # expression is "x" or "2"
            if expression.lstrip("-").isdigit():
                return int(expression)
            else: 
                return scope[expression]
        cur = expression[0]
        expression = expression[1:]
        # use scope.copy() to avoid modifying the outer scope 
        if cur == "let": 
            while len(expression) > 2: 
                scope = self.letExp(expression, scope.copy())
                expression = expression[2:]
            return self.calExp(expression[0], scope.copy())
        elif cur == "add":
            return self.addExp(expression, scope.copy())
        elif cur == "mult":
            return self.multExp(expression, scope.copy())
    def evaluate(self, expression: str) -> int:
        exp_list = self.parseExp(expression)
        result = self.calExp(exp_list, {})
        return result
        
if __name__ == "__main__": 
    s = Solution()

    # expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
    # assert s.evaluate(expression) == 14 

    # expression = "(let a1 3 b2 (add a1 1) b2)"
    # assert s.evaluate(expression) == 4 

    expression = "(let x 7 -12)"
    assert s.evaluate(expression) == -12