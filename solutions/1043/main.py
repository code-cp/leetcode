from typing import * 

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # init: dp[0] = 0, and valid i starts at 1
        # this is because in the first partition we can have arr[0] 
        dp = [0]*(n+1)
        for i in range(1, n+1): 
            # reset max_val for each i  
            max_val = -1
            # partition: xxx j | xxx i, eg j = 1, i = 2 => 1 | 15
            # j min val is 0, so end at max(-1, i-k-1) 
            # last val is xxx i-k | xxx i
            # numbers in cur partition when k = 2 is 
            # [i-1, i], whose len is 2 
            for j in range(i-1, max(-1, i-k-1), -1): 
                max_val = max(max_val, arr[j])
                dp[i] = max(dp[i], dp[j]+max_val*(i-j))
        return dp[-1]
            
if __name__ == "__main__": 
    s = Solution() 
    arr = [1,15,7,9,2,5,10]
    k = 3
    assert s.maxSumAfterPartitioning(arr, k) == 84 