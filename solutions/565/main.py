from typing import * 

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        max_len = 0 
        for i, n in enumerate(nums): 
            count = 1 
            if visited[n] == -1:
                max_len = max(max_len, count)
                continue 
            visited[n] = -1
            j = nums[n]
            while visited[j] != -1:
                visited[j] = -1
                count += 1  
                j = nums[j]
            max_len = max(max_len, count)
        return max_len

if __name__ == "__main__": 
    s = Solution()

    nums = [5,4,0,3,1,6,2]
    assert s.arrayNesting(nums) == 4 

    nums = [0,1,2]
    assert s.arrayNesting(nums) == 1 

    nums = [0,2,1]
    assert s.arrayNesting(nums) == 2 