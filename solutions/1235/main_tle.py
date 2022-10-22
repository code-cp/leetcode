from typing import * 

# Sort the elements by starting time, 
# then define the dp[i] as the maximum profit taking elements from the suffix starting at i.
# Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        keys = sorted(range(len(startTime)), key=lambda k: (startTime[k], profit[k]))
        startTime = [startTime[x] for x in keys]
        endTime = [endTime[x] for x in keys]
        profit = [profit[x] for x in keys]

        n = len(keys)
        dp = [0] * n 

        def bsearch(start, target): 
            left, right = start, n-1
            while left <= right: 
                mid = (right-left)//2 + left 
                if startTime[mid] < target:
                    left = mid + 1 
                else: 
                    right = mid - 1 
            return left 

        i = n-1 
        while i > -1: 
            j = bsearch(i+1, endTime[i])
            if j < n: 
                dp[i] = profit[i] + max(dp[j:])
            else: 
                dp[i] = profit[i]
            i -= 1 
                
        return max(dp)


if __name__ == "__main__": 
    s = Solution()

    startTime = [4,2,4,8,2]
    endTime = [5,5,5,10,8]
    profit = [1,2,8,10,4]
    assert s.jobScheduling(startTime, endTime, profit) == 18

    startTime = [1,2,2,3]
    endTime = [2,5,3,4]
    profit = [3,4,1,2]
    assert s.jobScheduling(startTime, endTime, profit) == 7

    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    assert s.jobScheduling(startTime, endTime, profit) == 150 

    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    assert s.jobScheduling(startTime, endTime, profit) == 120 