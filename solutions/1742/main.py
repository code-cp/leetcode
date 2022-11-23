
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        nums = [0]*(6*9)
        
        def digitsSum(digits): 
            res = 0 
            while digits > 0:
                res += digits % 10  
                digits //= 10 
            return int(res) 

        for i in range(lowLimit, highLimit+1): 
            s = digitsSum(i)
            nums[s] += 1 

        return max(nums)


if __name__ == "__main__": 
    s = Solution() 

    assert s.countBalls(220, 548) == 32 
    assert s.countBalls(1, 10) == 2 
