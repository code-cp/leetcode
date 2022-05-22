from typing import * 

class Solution:
    def bsearch(self, bars, idx, left=True): 
        l, r = 0, len(bars)-1 

        # l == r == mid is valid 
        while l <= r: 
            mid = (r-l)//2 + l
            if bars[mid] < idx: 
                # mid is invalid
                l = mid + 1 
            elif bars[mid] > idx:
                r = mid - 1 
            else: 
                return bars[mid]  
        
        if left: 
            if bars[mid] < idx: 
                mid += 1
        else: 
            if bars[mid] > idx: 
                mid -= 1 
        if mid > len(bars)-1 or mid < 0: 
            return -1 
        else: 
            return bars[mid]
                    
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        bars = []
        prefix_sum = [0] * len(s)
        count = 0 
        for i in range(len(s)): 
            if s[i] == "*":
                count += 1
            if s[i] == "|":
                prefix_sum[i] = count 
                bars.append(i)

        answer = [0] * len(queries)
        if len(bars) == 0: 
            return answer

        for i in range(len(queries)):
            q = queries[i]
            l = self.bsearch(bars, q[0])
            r = self.bsearch(bars, q[1], False)
            if l == -1 or r == -1 or r < l:
                answer[i] = 0 
            else: 
                answer[i] = prefix_sum[r] - prefix_sum[l]
        
        return answer

if __name__ == "__main__": 
    sol = Solution()

    s = "**|**|***|"
    queries = [[2,5],[5,9]]
    ans = [2,3]
    result = sol.platesBetweenCandles(s, queries)
    assert result == ans

    s = "***|**|*****|**||**|*"
    queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    ans = [9,0,0,0,0]
    result = sol.platesBetweenCandles(s, queries)
    assert result == ans

    s = "*|*||||**|||||||*||*||*||**|*|*||*"
    queries = [[2,33],[2,32],[3,31],[0,33],[1,24],[3,20],[7,11],[5,32],[2,31],[5,31],[0,31],[3,28],[4,33],[6,29],[2,30],[2,28],[1,30],[1,33],[4,32],[5,30],[4,23],[0,30],[3,10],[5,28],[0,28],[4,28],[3,33],[0,27]]
    ans = [9,9,9,10,6,4,0,9,9,9,10,7,9,8,8,7,9,10,9,8,5,9,2,7,8,7,9,8]
    result = sol.platesBetweenCandles(s, queries)
    assert result == ans

    s = "||*"
    queries = [[2,2]]
    ans = [0]
    result = sol.platesBetweenCandles(s, queries)
    assert result == ans

    s = "***"
    queries = [[2,2]]
    ans = [0]
    result = sol.platesBetweenCandles(s, queries)
    assert result == ans