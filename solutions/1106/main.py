from collections import deque 
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        n = len(expression)
        stack = deque()
        for e in expression: 
            # push 
            if e != ")":
                if e == "f" or e == "t": 
                    if len(stack[-1]) < 2:
                        stack.append([0, 0])
                    if e == "f": 
                        stack[-1][0] += 1 
                    else: 
                        stack[-1][1] += 1 
                elif e != "," and e != "(": 
                    stack.append(e)
            else: 
                # pop 
                f_total = t_total = 0 
                while len(stack[-1]) > 1:
                    f, t = stack[-1]
                    stack.pop()
                    f_total += f 
                    t_total += t 
                f, t = f_total, t_total

                opt = stack[-1]
                stack.pop()
                if opt == "|": 
                    if t != 0: 
                        stack.append([0, 1])
                    else: 
                        stack.append([1, 0])
                elif opt == "&": 
                    if f != 0: 
                        stack.append([1, 0])
                    else: 
                        stack.append([0, 1])  
                else: 
                    if t != 0: 
                        stack.append([1, 0])
                    else: 
                        stack.append([0, 1]) 

        f, t = stack[-1]
        return t > 0 

if __name__ == "__main__": 
    s = Solution()

    expression = "|(&(t,f,t),!(t))"
    assert not s.parseBoolExpr(expression)

    expression = "!(&(f,t))"
    assert s.parseBoolExpr(expression)

    expression = "|(f,f,f,t)"
    assert s.parseBoolExpr(expression)

    expression = "&(|(f))"
    assert not s.parseBoolExpr(expression)



                    




