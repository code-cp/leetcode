from typing import * 

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = [i[0] for i in sorted(enumerate(arr), key=lambda arr: arr[1])]
        res = [0] * len(arr)
        a = sorted(arr)
        for i in range(len(arr)):
            if i == 0: 
                pre_idx = 0 
            elif arr[arr_sorted[i]] == pre:
                pass 
            else: 
                pre_idx += 1  
            res[arr_sorted[i]] = pre_idx+1 
            pre = arr[arr_sorted[i]]
        return res 

if __name__ == "__main__": 
    s = Solution()

    # arr = [40,10,20,30]
    # assert s.arrayRankTransform(arr) == [4,1,2,3]

    # arr = [100,100,100]
    # assert s.arrayRankTransform(arr) == [1,1,1]

    arr = [37,12,28,9,100,56,80,5,12]
    assert s.arrayRankTransform(arr) == [5,3,4,2,8,6,7,1,3]