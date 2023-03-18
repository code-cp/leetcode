from typing import * 

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        res = [0]*m 
        for i in range(m):
            if queries[i] < nums[0]: 
                continue 
            total = nums[0]
            j = 0 
            while j < (n-1) and total <= queries[i]:
                j += 1 
                total += nums[j]
            if total > queries[i]: 
                j -= 1 
            res[i] = j+1 
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    nums = [4,5,2,1]
    queries = [3,10,21]
    assert s.answerQueries(nums, queries)
            