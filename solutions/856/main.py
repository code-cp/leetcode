from collections import deque 
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def isBalanced(s: str) -> bool:
            stack = deque()
            for i in range(len(s)): 
                if s[i] == "(":
                    stack.append(s[i])
                else: 
                    if len(stack) == 0: 
                        return False 
                    stack.pop()
            return len(stack) == 0

        # base case 
        if s == "()":
            return 1 
        if isBalanced(s[1:-1]):
            return 2*self.scoreOfParentheses(s[1:-1])
            
        total = 0 
        stack = deque()
        cur = ""
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                cur += s[i]
            else: 
                stack.pop()
                cur += ")"
                if len(stack) == 0: 
                    total += self.scoreOfParentheses(cur)
                    cur = ""
        return total 

if __name__ == "__main__": 
    sol = Solution()

    s = "(())(())"
    assert sol.scoreOfParentheses(s) == 4 

    s = "(())()"
    assert sol.scoreOfParentheses(s) == 3 

    s = "(()(()))"
    assert sol.scoreOfParentheses(s) == 6 

    s = "(())"
    assert sol.scoreOfParentheses(s) == 2 

    s = "()()"
    assert sol.scoreOfParentheses(s) == 2 