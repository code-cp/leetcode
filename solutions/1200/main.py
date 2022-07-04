from typing import * 

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        n = len(arr)
        for i in range(1, n): 
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff 
        res = []
        for i in range(1, n): 
            diff = arr[i] - arr[i-1]
            if diff == min_diff:
                res.append([arr[i-1], arr[i]])
        return res 

if __name__ == "__main__": 
    s = Solution()
    
    arr = [4,2,1,3]
    assert s.minimumAbsDifference(arr) == [[1,2],[2,3],[3,4]]

