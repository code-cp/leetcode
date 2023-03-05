
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n-1)
        left = time % (n-1)
        if cycle % 2 == 0: 
            # at start 
            res = 0 
            res += left + 1 
        else: 
            # at end 
            res = n 
            res -= left 
        return res

if __name__ == "__main__": 
    s = Solution() 

    assert s.passThePillow(3, 2) == 3 
    # assert s.passThePillow(4, 5) == 2 