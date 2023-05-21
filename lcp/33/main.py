from typing import * 
import math 
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        max_fill_all_opt = max(vat)
        if max_fill_all_opt == 0: 
            return 0 
        res = float("inf")
        for k in range(1, max_fill_all_opt+1): 
            fill_bucket_opt = 0 
            for i in range(n): 
                fill_bucket_opt += max(0, math.ceil(vat[i]/k) - bucket[i])
            res = min(res, fill_bucket_opt + k)
        return res  

if __name__ == "__main__": 
    s = Solution() 

    bucket = [16,29,42,70,42,9]
    vat = [89,44,50,90,94,91]
    assert s.storeWater(bucket, vat) == 11

    bucket = [9,0,1]
    vat = [0,2,2]
    assert s.storeWater(bucket, vat) == 3
    
    bucket = [1,3]
    vat = [6,8]
    assert s.storeWater(bucket, vat) == 4 

            