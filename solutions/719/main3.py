
# wrong 
import heapq 
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
            heapq.heappush(pq, (nums[i]-nums[i-1], i-1, i))
        while len(pq) > 0: 
            diff, i, j = heapq.heappop(pq) 
            k -= 1 
            if k == 0: 
                return diff
            if j < n-1:  
                heapq.heappush(pq, (nums[j+1]-nums[i], i, j+1))
            if i > 0:
                heapq.heappush(pq, (nums[j]-nums[i-1], i-1, j))
        
if __name__ == "__main__": 
    s = Solution()

    assert s.smallestDistancePair([1,3,1], 1) == 0

    assert s.smallestDistancePair([1,6,1], 3) == 5

    assert s.smallestDistancePair([62,100,4], 2) == 58