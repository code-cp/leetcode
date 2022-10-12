class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1 = set()
        diff2 = set()
        count = 0 
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                diff1.add(s1[i])
                diff2.add(s2[i])
                count += 1 
        if not (count == 0 or count == 2): 
            return False 
        if count != 0:
            if diff1 != diff2: 
                return False 
        return True 

if __name__ == "__main__": 
    s = Solution() 

    s1 = "caa"
    s2 = "aaz"
    assert s.areAlmostEqual(s1, s2)

    s1 = "bank"
    s2 = "kanb"
    assert s.areAlmostEqual(s1, s2)