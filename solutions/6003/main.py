from re import T
from typing import List 

class Solution:
    def minimumTime(self, s: str) -> int:
        # preprocess 
        s = [int(x) for x in s]
        n = len(s)
        # assume only type 1 can be used 
        # from left to right 
        dp_prefix = [0] * n 
        dp_prefix[0] = s[0]
        diff = 1-s[0]
        for i in range(1, n): 
            diff += 1
            dp_prefix[i] = dp_prefix[i-1] + diff * s[i]
            if s[i] == 1: 
                diff = 0

        # assume only type 2, 3 can be used 
        # from right to left 
        dp_suffix = [0] * n 
        dp_suffix[-1] = s[-1]
        for i in range(n-2, -1, -1): 
            if s[i] == 0: 
                dp_suffix[i] = dp_suffix[i+1]
            else:
                dp_suffix[i] = min(dp_suffix[i+1]+2, n-i)

        # combine the above 
        result = float("inf")
        if n == 1: 
            return dp_prefix[0]
        for i in range(n-1): 
            result = min(result, dp_prefix[i] + dp_suffix[i+1])
        return result

if __name__ == "__main__": 
    s = "1100101"
    sol = Solution()
    assert sol.minimumTime(s) == 5

