from typing import * 

class Solution:
    def backtrack(self, s, idx, num, cur):
        if len(cur) == 0: 
            cur += "("
        if len(num) > 1: 
            if num[:2] == "00":
                return 

        if idx < len(s):
            if len(num) != 0:
                # start a new number 
                if len(cur) == 1:
                    if len(num) > 1 and float(num) == 0:
                        pass 
                    elif len(num) > 1 and num[0] == "0" and num[1] != ".": 
                        pass 
                    else:
                        self.backtrack(s, idx+1, s[idx], cur+num)
                else: 
                    self.backtrack(s, idx+1, s[idx], cur+", "+num)
            # keep adding to cur number 
            self.backtrack(s, idx+1, num+s[idx], cur)
            if len(num) > 0 and "." not in num:
                self.backtrack(s, idx+1, num+"."+s[idx], cur)
        else: 
            if len(cur) == 1 or cur.count(',') > 0: 
                return 
            cur += ", "
            cur += num 
            cur += ")"
            self.res.append(cur)
            return 

    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:]
        s = s[:-1]
        self.res = []
        self.backtrack(s, 0, "", "")
        return self.res 

if __name__ == "__main__": 
    sol = Solution()  

    s = "(100)"
    print(sol.ambiguousCoordinates(s))

    s = "(00011)"
    print(sol.ambiguousCoordinates(s))

    s = "(0123)"
    print(sol.ambiguousCoordinates(s))

    s = "(123)"
    print(sol.ambiguousCoordinates(s))
