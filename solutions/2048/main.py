from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # generate all balanced nums 
        nums = [1,22,333,4444,55555,666666]
        perm = []
        for p in ["122", "1333", "14444", "22333", "122333", "155555", "224444"]:
            perm.extend(list(permutations(p)))
        nums.extend([int("".join(p)) for p in perm])
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        nums.append(1224444)
        
        l, r = 0, len(nums)-1
        while l <= r: 
            mid = (r-l)//2+l 
            if nums[mid] > n: 
                r = mid-1 
            else: 
                l = mid+1 
        
        return nums[l]
    
if __name__ == "__main__": 
    s = Solution()
    
    s.nextBeautifulNumber(1)