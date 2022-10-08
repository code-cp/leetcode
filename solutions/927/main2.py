from typing import * 
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # find number of 1  
        one_cnt, mod = divmod(sum(arr), 3)
        # no. of 1 must be multiple of 3 
        if mod != 0: 
            return [-1, -1]
        # if all 0, return 
        if one_cnt == 0: 
            # 3 <= arr.length <= 3 * 104
            return [0, 2]
        n = len(arr)
        pre_sum = [0] * n
        cnt = 0  
        for i in range(n):
            cnt += arr[i]
            pre_sum[i] = cnt  

        def bsearch(target): 
            left, right = 0, n-1 
            while left <= right:
                mid = (right-left)//2 + left 
                # NOTE, find first index such that pre_sum equals target 
                if pre_sum[mid] < target: 
                    left = mid+1 
                else: 
                    right = mid-1 
            return left 
        # skip the leading zeros 
        i, j, k = bsearch(1), bsearch(one_cnt+1), bsearch(one_cnt*2 + 1)
        while k < n and arr[i] == arr[j] == arr[k]: 
            i += 1 
            j += 1 
            k += 1 
        return [i-1, j] if k == len(arr) else [-1, -1]

if __name__ == "__main__": 
    s = Solution() 

    arr = [1,1,0,0,1]
    assert s.threeEqualParts(arr) == [0,2]

    arr = [1,0,1,0,1]
    assert s.threeEqualParts(arr) == [0,3]



        




