
# wrong 
from queue import PriorityQueue
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            pq.append((i-1, i, nums[i]-nums[i-1]))
        while len(pq) > 0: 
            i, j, diff = pq.pop(0) 
            k -= 1 
            if k == 0: 
                return diff
            if j < n-1:  
                pq.append((i, j+1, nums[j+1]-nums[i]))
            if i > 0:
                pq.append((i-1, j, nums[j]-nums[i-1]))
        
if __name__ == "__main__": 
    s = Solution()

    # assert s.smallestDistancePair([1,6,1], 3) == 5

    assert s.smallestDistancePair([62,100,4], 2) == 58