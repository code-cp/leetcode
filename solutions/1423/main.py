from typing import * 

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.
        # Keep a window of size n - k over the array. The answer is max(answer, total_pts - sumOfCurrentWindow)
        
        n = len(cardPoints)
        win_size = n-k 
        total = sum(cardPoints)
        # NOTE, since we use win_size-1 later, need to check if win_size is 0 
        if win_size == 0: 
            return total 
        
        res = 0 
        left, right = 0, win_size-1 
        cur_sum = sum(cardPoints[left:right])
        while right < n: 
            # add new element 
            cur_sum += cardPoints[right]
            res = max(res, total - cur_sum)
            # discard element outside win 
            cur_sum -= cardPoints[left]
            left += 1 
            right += 1 
        
        return res 
    
if __name__ == "__main__": 
    s = Solution()
  
    assert s.maxScore([1,1000,1], 1) == 1 
    assert s.maxScore([9,7,7,9,7,7,9], 7) == 55 
    assert s.maxScore([1,2,3,4,5,6,1], 3) == 12 