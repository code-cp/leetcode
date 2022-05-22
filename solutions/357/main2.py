# time 1808 ms
class Solution:
    def backtracking(self, n, step, bitmask, num): 
        # base case 
        if step == n: 
            return  

        for i in range(0, 10): 
            # NOTE, this is not bitmask & 1 << i == 1
            if bitmask >> i & 1 == 1: 
                continue 
            if self.debug: 
                num.insert(0, i)
            if i != 0: 
                self.valid += 1
                if self.debug: 
                    self.nums.append([x for x in num])
            self.backtracking(n, step+1, bitmask | (1 << i), num)
            if self.debug:
                num.pop(0)

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.valid = 1 
        self.nums = []
        self.debug = False 
        self.backtracking(n, 0, 0, []) 
        return self.valid 

if __name__ == "__main__": 
    s = Solution() 

    # n = 1
    # result = s.countNumbersWithUniqueDigits(n) 
    # assert result == 10 

    n = 2 
    result = s.countNumbersWithUniqueDigits(n) 
    assert result == 91 