from typing import * 

class Solution:
    @staticmethod 
    def checkPrimes(num, primes): 
        state = 0 
        for j, p in enumerate(primes): 
            if num % (p ** 2) == 0: 
                return -1 
            if num % p == 0: 
                state |= (1 << j)
        return state 

    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mod = 10**9 + 7
        freq = Counter(nums)
        # dp table 
        dp = [[0] * (1 << len(primes)) for _ in range(31)] 
        # initialize 
        dp[1][0] = (2 ** freq[1]) % mod 
        # traverse 
        for i in range(2, 31): 
            subset = self.checkPrimes(i, primes)
            for state in range(1 << len(primes)): 
                if subset == -1 or (state & subset) != subset:
                    dp[i][state] = dp[i-1][state] % mod 
                # make sure state contains subset 
                else: 
                    dp[i][state] = (dp[i-1][state] + dp[i-1][state^subset] * freq[i]) % mod 
        # get results 
        result = sum(dp[30][1:]) % mod 
        return result

if __name__ == "__main__": 
    nums = [4,2,3,15]
    s = Solution()
    assert s.numberOfGoodSubsets(nums) == 5