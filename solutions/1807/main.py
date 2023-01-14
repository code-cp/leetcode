from typing import * 

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        m = dict(knowledge)
        res = ""
        k = None
        for ch in s: 
            if ch == "(": 
                k = ""
            elif ch == ")": 
                v = m.get(k, None)
                k = None 
                if v is None: 
                    res += "?"
                else: 
                    res += v 
            elif k is not None: 
                k += ch 
            else: 
                res += ch 
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "(name)is(age)yearsold"
    knowledge = [["name","bob"],["age","two"]]
    assert sol.evaluate(s, knowledge) == "bobistwoyearsold"