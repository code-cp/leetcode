#         OR      XOR
# (0, 0)  0        0
# (0, 1)  1        1
# (1, 0)  1        1
# (1, 1)  1        0

# (0,0) -> (0,0)
# (0,1), (1,0) -> (1,1)
# (1,1) -> (1,0), (0,1)


from collections import Counter 
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        n = len(s)
        cnt = Counter(s)
        cnt0 = cnt["0"]
        cnt1 = cnt["1"]
        diff0 = 0 
        diff1 = 0 
        for i in range(n): 
            if s[i] == target[i]: 
                continue 
            if s[i] == "0": 
                diff0 += 1 
            else: 
                diff1 += 1 
        diff = min(diff0, diff1)
        diff0 -= diff 
        diff1 -= diff 
        
        for i in range(diff0): 
            if cnt1 <= 0: 
                return False 
            cnt0 -= 1 
            cnt1 += 1 

        for i in range(diff1): 
            if cnt1 <= 1: 
                return False 
            cnt0 += 1 
            cnt1 -= 1 

        return True 

if __name__ == "__main__": 
    sol = Solution() 

    s = "1010"
    target = "0110"
    assert sol.makeStringsEqual(s, target)

    s = "11"
    target = "00"
    assert not sol.makeStringsEqual(s, target)

    s = "001000"
    target = "000100"
    assert sol.makeStringsEqual(s, target)