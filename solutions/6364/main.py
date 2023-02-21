from typing import * 

from collections import Counter 
import math 

factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

class Solution:
    def checkfactors(self, num): 
        state = 0 
        for j, p in enumerate(factors): 
            if num % (p ** 2) == 0: 
                return -1 
            if num % p == 0: 
                state |= (1 << j)
        return state 

    def squareFreeSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        max_val = max(nums)
        if max_val == 1: 
            return (2**(len(nums))-1) % mod 

        freq = Counter(nums)
        # dp table 
        dp = [[0] * (1 << len(factors)) for _ in range(31)] 
        # initialize 
        dp[1][0] = (2 ** freq[1]) % mod 
        # traverse 
        for i in range(2, 31): 
            subset = self.checkfactors(i)
            for state in range(1 << len(factors)): 
                if subset == -1 or (state & subset) != subset:
                    dp[i][state] = dp[i-1][state] % mod 
                # make sure state contains subset 
                else: 
                    dp[i][state] = (dp[i-1][state] + dp[i-1][state^subset] * freq[i]) % mod 
        # get results 
        result = sum(dp[30][1:]) % mod 
        if dp[1][0] > 0:
            result += dp[1][0] - 1 
            result %= mod 
        return result

if __name__ == "__main__": 
    s = Solution() 

    nums = [17,27,20,1,19]
    assert s.squareFreeSubsets(nums) == 7 

    nums = [1]
    assert s.squareFreeSubsets(nums) == 1 

    nums = [3,4,4,5]
    assert s.squareFreeSubsets(nums) == 3 