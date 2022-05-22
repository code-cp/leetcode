from typing import List 

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        st = [0]
        for i in range(1, len(nums)):
            while len(st) != 0 and nums[st[-1]] < nums[i]:
                result[st[-1]] = nums[i]
                st = st[:-1]
            st.append(i)
        for i in range(len(nums)):
            while len(st) != 0 and nums[st[-1]] < nums[i]:
                if result[st[-1]] == -1:
                    result[st[-1]] = nums[i]
                st = st[:-1]
        return result

if __name__ == "__main__": 
    nums = [1,2,3,4,3]
    ans = [2,3,4,-1,4]
    s = Solution()
    assert s.nextGreaterElements(nums) == ans 
