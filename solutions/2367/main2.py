from typing import * 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hashmap_parents = {}
        hashmap_count = {}
        n = len(nums)
        # union find 
        # no union, only find 
        for i in range(n): 
            num = nums[i]-diff 
            if num in hashmap_parents: 
                j = hashmap_parents[num]
                hashmap_count[j] = hashmap_count.get(j, 0)+1  
                hashmap_parents[nums[i]] = j 
            else: 
                hashmap_parents[nums[i]] = i 
        res = 0 
        for k, v in hashmap_count.items(): 
            if v >= 2: 
                res += v-1 
        return res 