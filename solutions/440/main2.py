from typing import * 
import math 

class Solution:
    def countPrefix(self, cur_prefix, level, n):
        count = 0 
        if cur_prefix > n: 
            return count
        # count current prefix 
        count += 1 
        if cur_prefix == n//level:
            # if cur_prefix is prefix of n 
            for i in range(10): 
                count += self.countPrefix(cur_prefix*10+i, level/10, n)
        else: 
            # if cur_prefix is not prefix of n 
            count += 10 * self.countPrefix(cur_prefix*10, level/10, n) 
        return count 
    def findKthNumber(self, n: int, k: int) -> int:
        cur_prefix = 1 
        k -= 1 
        while k > 0: 
            # find the current recursion level 
            exp = math.floor(math.log10(n//cur_prefix))
            level = 10 ** exp  
            # count the prefix 
            count = self.countPrefix(cur_prefix, level, n)
            if k < count: 
                cur_prefix *= 10 
                k -= 1
            else: 
                cur_prefix += 1 
                k -= count
        return cur_prefix 

if __name__ == "__main__": 
    s = Solution()

    # n = 13
    # k = 2
    # assert s.findKthNumber(n, k) == 10

    n = 9885387
    k = 8786251
    assert s.findKthNumber(n, k) == 8907623
