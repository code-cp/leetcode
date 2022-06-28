from typing import * 

# time O(nlogn)
# space O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_sort = sorted(nums)
        n = len(nums_sort)
        min_nums = nums_sort[:n//2]
        min_nums = min_nums[::-1]
        max_nums = nums_sort[n//2:]
        max_nums = max_nums[::-1]
        
        if n % 2 == 1: 
            n -= 1 
            nums[-1] = max_nums[-1]

        for i in range(n):
            if i % 2 == 0: 
                nums[i] = min_nums[i//2]
            else:
                nums[i] = max_nums[i//2]

        if n > 0 and nums[-1] == nums[-2]:
            j = 0 
            while j <= n and nums[j] == nums[-1]:
                j += 2 
            nums[j], nums[-1] = nums[-1], nums[j]

if __name__ == "__main__": 
    s = Solution()

    # nums = [1,5,1,1,6,4]
    # s.wiggleSort(nums)
    # print(nums)

    # nums = [1,3,2,2,3,1]
    # s.wiggleSort(nums)
    # print(nums)

    # nums = [1,1,2,1,2,2,1]
    # s.wiggleSort(nums)
    # print(nums)

    # nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
    # s.wiggleSort(nums)
    # print(nums)

    nums = [5,3,1,2,6,7,8,5,5]
    s.wiggleSort(nums)
    print(nums)