import math

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        gcd = math.gcd(a, b)
        return abs(a * b) / gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = []
        expr = expression.split("+")
        for i, e in enumerate(expr):
            sign = 1  
            te = e.split("-")
            for j, t in enumerate(te):
                if len(t) == 0:
                    continue 
                if j > 0: 
                    sign = -1 
                n = t.split("/")
                nums.append([sign*int(n[0]), int(n[1])])
                sign = 1

        denominator = 1
        for n in nums: 
            denominator = int(lcm(denominator, n[1]))
        numerator = 0 
        for n in nums: 
            numerator += n[0]*(denominator/n[1])
        gcd = math.gcd(int(numerator), denominator)
        numerator /= gcd 
        denominator /= gcd 
        res = str(int(numerator)) + "/" + str(int(denominator))
        return res 

if __name__ == "__main__": 
    s = Solution()

    # expression = "-1/2+1/2"
    # assert s.fractionAddition(expression) == "0/1"

    # expression = "1/3-1/2"
    # assert s.fractionAddition(expression) == "-1/6"
            
    expression = "-1/2+1/2+1/3"
    assert s.fractionAddition(expression) == "1/3"