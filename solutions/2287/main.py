from collections import Counter 
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(target)
        res = float("inf")
        for k, v in cnt2.items(): 
            if cnt1[k] < 1: 
                return 0 
            res = min(res, cnt1[k] // v)
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "ilovecodingonleetcode"
    target = "code"
    assert sol.rearrangeCharacters(s, target) == 2 