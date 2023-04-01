import re 
import itertools
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: 
            email = s.split("@")
            name = email[0][0].lower()+"*****"+email[0][-1].lower()
            domain = email[1].lower()
            return name+"@"+domain 
        else: 
            # NOTE, put - in first, ref https://stackoverflow.com/a/28539453/8519188
            separation = ['-','+', '(', ')', ' ']
            separation = "["+"".join(separation)+"]"
            phone = re.split(separation, s)
            phone = itertools.chain(phone)
            phone = "".join(phone)
            num = ""
            if len(phone) > 10:
                num += "+"
                num += "*"*(len(phone)-10)
                num += "-"
            num += "***-***-"
            num += phone[-4:]
            return num 
            
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.maskPII("LeetCode@LeetCode.com") == "l*****e@leetcode.com"
    assert s.maskPII("1(234)567-890") == "***-***-7890"