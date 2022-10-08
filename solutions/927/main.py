class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # check input 
        cnt, mod = divmod(sum(arr), 3)
        # no. of 1 must be multiple of 3 
        if mod != 0: 
            return [-1, -1]
        # if all 0, return 
        if cnt == 0: 
            return [0, 2]
        def find(x): 
            s = 0 
            for i, v in enumerate(arr):
                s += v 
                if s == x: 
                    return i 
        # 0 1 1 0 0 0 1 1 0 0 0 0 0 1 1 0 0
        #   ^         ^             ^
        #   i         j             k
        # 作者：lcbin
        # 链接：https://leetcode.cn/problems/three-equal-parts/solution/by-lcbin-7ir1/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        i, j, k = find(1), find(cnt+1), find(cnt*2 + 1)
        while k < len(arr) and arr[i] == arr[j] == arr[k]: 
            i, j, k = i+1, j+1, k+1 
        # 0 1 1 0 0 0 1 1 0 0 0 0 0 1 1 0 0
        #           ^         ^             ^
        #           i         j             k
        return [i-1, j] if k == len(arr) else [-1, -1]
