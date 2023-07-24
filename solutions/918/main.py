from typing import * 

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/1152143/wo-hua-yi-bian-jiu-kan-dong-de-ti-jie-ni-892u/comments/1278889
        # 最大子数组 不成环 --- 53题 也就是maxSum为答案
        # 最大子数组 成环 ，那么最小子数组就不会成环 --- (total - minSum) 则为答案
        
        # https://leetcode.cn/problems/maximum-sum-circular-subarray/discussion/comments/2069671
        # 分类讨论: 环形子数组的最大和是下面二者之一: 1)普通的子数组的最大和, 2)一个前缀加一个后缀构成的子数组的最大和. 求普通的子数组的最大和用经典dp: 设p[i]p[i]p[i]为以nums[i]nums[i]nums[i]为右端点的区间的最大子数组和, 有状态转移: p[i]=max(nums[i],nums[i]+p[i−1])p[i]=max(nums[i],nums[i]+p[i-1])p[i]=max(nums[i],nums[i]+p[i−1]); 求一个前缀加一个后缀构成的子数组的最大和可以枚举前缀和后缀的分割位置iii, 用 "nums[0,i]nums[0,i]nums[0,i]上的最大前缀和+nums[i+1,n−1]nums[i+1,n-1]nums[i+1,n−1]上的最大后缀和" 更新答案.
        
        total = sum(nums)
        
        n = len(nums)
        dp1 = [0]*(n+1) 
        for i in range(1, n+1): 
            dp1[i] = max(nums[i-1], dp1[i-1]+nums[i-1])
            
        dp2 = [float("inf")]*(n+1)
        for i in range(1, n+1): 
            dp2[i] = min(nums[i-1], dp2[i-1]+nums[i-1])
                
        res = max(max(dp1), total-min(dp2))
        
        # handle all negative nums 
        mx = max(nums)
        if res == 0 and mx < 0:
            return mx 
        
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.maxSubarraySumCircular([0,5,8,-9,9,-7,3,-2]) == 16
    # assert s.maxSubarraySumCircular([3,-1,2,-1]) == 4 
    # assert s.maxSubarraySumCircular([5,-3,5]) == 10
    # assert s.maxSubarraySumCircular([-3,-2,-3]) == -2 
    assert s.maxSubarraySumCircular([-10,-7,9,-7,6,9,-9,-4,-8,-5]) == 17 