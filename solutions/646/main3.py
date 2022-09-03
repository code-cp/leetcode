from typing import * 
# 二分
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def bsearch(arr, target):
            # insert after the first value < target 
            left, right = 0, len(arr)-1
            while left <= right: 
                mid = (right-left)//2 + left 
                if arr[mid] < target:  
                    left = mid+1
                else: 
                    right = mid-1
            return left 

        pairs.sort()
        arr = []
        for x, y in pairs: 
            i = bsearch(arr, x)
            if i < len(arr): 
                arr[i] = min(arr[i], y)
            else: 
                arr.append(y)
        return len(arr)
        

if __name__ == "__main__": 
    s = Solution()

    # pairs = [[1,2],[2,3],[3,4]]
    # assert s.findLongestChain(pairs) == 2 

    pairs = [[1,2],[7,8],[4,5]]
    assert s.findLongestChain(pairs) == 3 