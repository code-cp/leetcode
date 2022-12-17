from typing import * 

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        idx = i = j = 0 
        while idx < len(groups) and i < len(nums): 
            start = i 
            while j < len(groups[idx]) and i < len(nums): 
                if groups[idx][j] == nums[i]: 
                    j += 1 
                    i += 1 
                else: 
                    j = 0 
                    i = start + 1 
                    break 
                if j == len(groups[idx]): 
                    start = i 
                    j = 0 
                    idx += 1 
                    if idx == len(groups): 
                        break 
        return idx == len(groups)

if __name__ == "__main__": 
    s = Solution() 

    groups = [[1,2,3],[3,4]]
    nums = [7,7,1,2,3,4,7,7]
    assert not s.canChoose(groups, nums)

    # groups = [[1,-1,-1],[3,-2,0]]
    # nums = [1,-1,0,1,-1,-1,3,-2,0]
    # assert s.canChoose(groups, nums)

    # groups = [[10,-2],[1,2,3,4]]
    # nums = [1,2,3,4,10,-2]
    # assert not s.canChoose(groups, nums)