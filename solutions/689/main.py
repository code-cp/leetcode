from typing import List 

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # dp table
        dp = [[0]*len(nums) for _ in range(3)]
        path = [[0]*len(nums) for _ in range(3)]
        # initialize
        preSum = [0]*len(nums)
        winSum = 0
        for i in range(len(nums)):
            winSum += nums[i]
            if i >= k:
                winSum -= nums[i-k]
            if i >= k-1:
                preSum[i] = winSum

        maxSum = -float("inf")
        maxId = 0
        for i in range(len(nums)):
            winSum = preSum[i]
            if winSum > maxSum:
                maxSum = winSum
                if i >= k-1:
                    maxId = i-k+1
            path[0][i] = maxId
            dp[0][i] = maxSum

        # traverse dp table
        for i in range(1, 3):
            start = (i+1)*k-1
            maxSum = -float("inf")
            maxId = start
            for j in range(start, len(nums)):
                if maxSum < dp[i-1][j-k] + preSum[j]:
                    maxId = j
                    maxSum = dp[i-1][j-k] + preSum[j]
                dp[i][j] = maxSum
                path[i][j] = maxId-k+1

        result = [0]*3
        result[2] = path[2][-1]
        result[1] = path[1][result[2]-1]
        result[0] = path[0][result[1]-1]

        return result

if __name__ == "__main__": 
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    s = Solution()
    result = s.maxSumOfThreeSubarrays(nums, k)
    ans = [0,3,5]
    assert result == ans 
