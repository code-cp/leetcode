from typing import * 
from collections import Counter 

# cannot deal with 1,2,2,2,2,2,3,3,3,3,3,3,3,4,5...

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        max_v = max(list(cnt.values()))
        if max_v > k: 
            return -1 
        
        ans = float("inf")
        n = len(nums)
        visited = [0]*n 
        # sort nums 
        nums.sort()
        
        def dfs(cur_idx, count, low, high, incom_sum):
            nonlocal n 
            nonlocal k 
            nonlocal nums
            nonlocal ans 
            
            # base case 
            # nums.length is divisible by k
            if count == n//k: 
                j = 0 
                while j < n and visited[j] == 1:
                    j += 1 
                if j == n: 
                    # all k subsets are finished 
                    ans = min(ans, incom_sum + high - low)
                    return 
                visited[j] = 1 
                dfs(j, 1, nums[j], nums[j], incom_sum + high - low)
                # back track 
                visited[j] = 0 
            else: 
                # find next element for current subset 
                for i in range(cur_idx+1, n): 
                    if visited[i] == 1: 
                        continue 
                    # NOTE, nums is sorted 
                    if nums[i] == nums[cur_idx]: 
                        continue 
                    visited[i] = 1 
                    dfs(i, count+1, low, nums[i], incom_sum)
                    # back track 
                    visited[i] = 0 
                
            
        visited[0] = 1 
        dfs(0, 1, nums[0], nums[0], 0)

        return ans 

if __name__ == "__main__": 
    s = Solution()
    
    assert s.minimumIncompatibility([1,2,1,4], 2) == 4 