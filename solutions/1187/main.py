from typing import * 
import math 

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # dp[i][j], i is the element index, j is number of changes 
        # dp[i][j] means the min value of arr1[i]
        # dp[i-1][j] means already used j operations, so cannot change arr1[i]
        # ie dp[i-1][j] < arr1[i], dp[i][j] = arr1[i]
        # dp[i-1][j-1] means need to change arr1[i], so need to find a value in arr2 
        # that is smallest one > dp[i-1][j-1]
        
        # change to 1 index 
        arr1 = [0]+arr1 
        n = len(arr1)
        
        arr2.sort()
        def upperBound(target): 
            l, r = 0, len(arr2)-1
            while l <= r: 
                mid = (r-l)//2+l 
                if arr2[mid] <= target: 
                    l = mid+1 
                else: 
                    r = mid-1 
            return l 
        
        dp = [[float("inf")]*n for _ in range(n)]
        dp[0][0] = -float("inf")
        
        for i in range(1, n):
            for j in range(i+1): 
                if dp[i-1][j] < arr1[i]: 
                    dp[i][j] = min(dp[i][j], arr1[i])
                
                if j == 0: 
                    continue 
                
                idx = upperBound(dp[i-1][j-1])
                if idx != len(arr2): 
                    dp[i][j] = min(dp[i][j], arr2[idx])
                 
        for j in range(n): 
            if math.isfinite(dp[n-1][j]):
                return j 
                
        return -1 
        
if __name__ == "__main__": 
    s = Solution()   

    arr1 = [1,5,3,6,7]
    arr2 = [4,3,1]
    assert s.makeArrayIncreasing(arr1, arr2) == 2

    # arr1 = [1,5,3,6,7]
    # arr2 = [1,3,2,4]
    # assert s.makeArrayIncreasing(arr1, arr2) == 1