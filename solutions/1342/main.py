class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0: 
            if num & 1 == 1: 
                num -= 1 
            else: 
                num >>= 1
            result += 1 
        return result 

if __name__ == "__main__": 
    num = 14
    s = Solution()
    assert s.numberOfSteps(num) == 6
