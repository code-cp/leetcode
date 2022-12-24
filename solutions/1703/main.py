from typing import * 

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = []
        for i, n in enumerate(nums): 
            if n == 1: 
                ones.append(i)
        
        total = 0
        for i in range(k): 
            total += abs(ones[i]-ones[k//2])
        res = total 

        for i in range(len(ones)-k): 
            mid = i+k//2 
            total -= abs(ones[i]-ones[mid])
            total += abs(ones[i+k]-ones[mid+1])
            total += k//2*(ones[mid+1]-ones[mid])
            total -= (k-k//2-1)*(ones[mid+1]-ones[mid])
            res = min(res, total)

        offset = 0 
        for i in range(k): 
            offset += abs(i-k//2)

        return res-offset 

if __name__ == "__main__": 
    s = Solution() 

    nums = [1,0,0,1,0,1]
    k = 2
    assert s.minMoves(nums, k)