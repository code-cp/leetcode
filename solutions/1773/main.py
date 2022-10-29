from typing import * 

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0 

        name_dict = {
            "type": 0, 
            "color": 1, 
            "name": 2, 
        }

        for i in items: 
            if i[name_dict[ruleKey]] == ruleValue: 
                res += 1 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    assert s.countMatches(items, ruleKey, ruleValue) == 1 