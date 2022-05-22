# -*- coding: utf-8 -*-
"""
leetcode 15 3sum.ipynb
可以问面试官的问题：数组中是否存在重复的数，比如[0, 0, 0, 0]
需要注意的点：
- 使用while loop跳过重复的元素
- Python中for loop无法更改counter，跟cpp的for loop不同
- 可以使用hash set记录遍历过的数，减少一个counter的使用
"""


"""解法1 时间复杂度O(n^2)， 空间复杂度O(n)"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ret = []
        
        # base case 
        if len(nums) < 3:
            return ret; 
        
        # this is still necessary since we want to use while loop to skip duplicated elements 
        # sort array 
        # time O(nlogn), space O(1)
        nums = sorted(nums)

        # find sum
        # time O(n^2), space O(n)
        i = 0 
        while (i < len(nums)):
            j = i + 1
            temp = set()
            while (j < len(nums)):
                if (0 - nums[i] - nums[j] in temp):
                    curr = []
                    curr.append(nums[i])
                    curr.append(nums[j])
                    curr.append(0 - nums[i] - nums[j])
                    
                    ret.append(curr)
                    
                    while (j < len(nums) - 1 and nums[j] == nums[j+1]):
                        j += 1
                    
                else:
                    temp.add(nums[j])
                
                j += 1 
                
            while (i < len(nums) - 1 and nums[i] == nums[i+1]):
                i += 1 
            i += 1 
                    
        return ret

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))

"""解法2 时间复杂度O(n^2)，空间复杂度O(n)"""

class Solution(object):
    def threeSum(self, nums):
        
        # define the return value 
        ret = []
        
        # handle the invalid case 
        if (len(nums) < 3):
            return ret; 
        
        nums = sorted(nums)
        
        # first index  
        for i in range(len(nums) - 1):
            
            if (i > 0 and nums[i] == nums[i-1]):
                continue 
            
            # second index 
            j = i + 1 
            # third index 
            k = len(nums) - 1
            while (j < k):
                curr = []
                if (nums[i] + nums[j] + nums[k] == 0):
                    curr.append(nums[i])
                    curr.append(nums[j])
                    curr.append(nums[k])
                    ret.append(curr)
                    j += 1 
                    k -= 1 
                    while (j < k and nums[j-1] == nums[j]):
                        j += 1 
                    while (j < k and nums[k] == nums[k+1]):
                        k -= 1 
                elif (nums[i] + nums[j] + nums[k] < 0):
                    j += 1 
                else:
                    k -= 1 
                
        return ret

s = Solution()
nums = [-1,0,1,2,-1,-4]
print(s.threeSum(nums))