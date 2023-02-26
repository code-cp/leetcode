from collections import Counter 
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        diff = []
        for a, b in zip(s1, s2): 
            if a != b: 
                diff.append(a)
        cnt = Counter(diff)

        res = 0 
        # swap xx, yy 
        res += cnt["x"] // 2
        # swap yy, xx  
        res += cnt["y"] // 2
        if cnt["x"] % 2 != cnt["y"] % 2:
            return -1 
        # swap xy, yx 
        res += (cnt["x"] % 2) * 2 
        return res 
        


if __name__ == "__main__": 
    s = Solution() 

    s1 = "xy"
    s2 = "yx"
    assert s.minimumSwap(s1, s2) == 2 