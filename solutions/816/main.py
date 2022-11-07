from typing import * 

class Solution:
    def checkNum(self, num): 
        if len(num) > 1 and float(num) == 0: 
            return False 
        if len(num) > 1 and "." not in num and num[0] == "0":
            return False
        if len(num) > 1: 
            if num[:2] == "00":
                return False
            if num[0] == "0" and num[1] != "0" and num[1] != ".": 
                return False 
        if len(num) > 2 and "." in num:
            temp = num.split(".")
            if int(temp[-1]) == 0:
                return False 
            else:
                if temp[-1][-1] == "0":
                    return False 
        return True 

    def addDot(self, num):
        res = [num] 
        if len(num) == 1: 
            return res 
        for i in range(1, len(num)): 
            cur = num[:i] + "." + num[i:]
            res.append(cur)
        return res 

    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:]
        s = s[:-1]
        res = []

        for i in range(1, len(s)): 
            num1, num2 = s[:i], s[i:]
            nums1, nums2 = self.addDot(num1), self.addDot(num2)
            for n1 in nums1: 
                if not self.checkNum(n1): 
                    continue 
                for n2 in nums2: 
                    if not self.checkNum(n2): 
                        continue 
                    res.append("(" + n1 + ", " + n2 + ")")

        return res 
        
if __name__ == "__main__": 
    sol = Solution()  

    s = "(001)"
    print(sol.ambiguousCoordinates(s))

    s = "(100)"
    print(sol.ambiguousCoordinates(s))

    s = "(00011)"
    print(sol.ambiguousCoordinates(s))

    s = "(0123)"
    print(sol.ambiguousCoordinates(s))

    s = "(123)"
    print(sol.ambiguousCoordinates(s))
