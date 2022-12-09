class Solution:
    def checkPowersOfThree(self, n: int) -> bool: 
        while n > 0: 
            residual = n % 3 
            if residual == 2: 
                return False 
            n -= residual 
            n /= 3 
        return True 

if __name__ == "__main__": 
    s = Solution() 

    # assert s.checkPowersOfThree(12)
    assert not s.checkPowersOfThree(21)
