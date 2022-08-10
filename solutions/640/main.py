import re
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(eq): 
            x_co, num = 0, 0 
            for e in eq: 
                sign1 = 1 
                if e[0] == "-":
                    sign1 = -1 
                    e = e[1:]
                term = e.split("-")
                for i, t in enumerate(term): 
                    if "x" in t:
                        if t == "x":
                            c = 1 
                        else: 
                            c = int(t.split("x")[0]) 
                        if i == 0:
                            c *= sign1 
                        else: 
                            c *= -1
                        x_co += c 
                    else: 
                        c = int(t)
                        if i == 0:
                            c *= sign1 
                        else: 
                            c *= -1 
                        num += c 
            return x_co, num
                    
        terms = equation.split("=")
        
        lhs = terms[0].split("+")
        rhs = terms[1].split("+")

        lx, ln = parse(lhs)
        rx, rn = parse(rhs)

        x_co = lx - rx 
        n = rn - ln 

        if x_co == 0 and n == 0: 
            return "Infinite solutions"
        if x_co == 0 and n != 0: 
            return "No solution"
        if n == 0: 
            return "x=0"
        ans = n / x_co 
        res = "x=" + str(int(ans))
        return res

if __name__ == "__main__": 
    s = Solution()

    # equation = "x+5-3+x=6+x-2"
    # assert s.solveEquation(equation) == "x=2"

    # equation = "2x=x"
    # assert s.solveEquation(equation) == "x=0"

    # equation = "x=x+2"
    # assert s.solveEquation(equation) == "No solution"

    equation = "-x=-1"
    assert s.solveEquation(equation) == "x=1"