from typing import * 

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_t = 0 
        max_idx = float("inf")
        t_pre = 0 
        for idx, t in logs:
            if t-t_pre > max_t: 
                max_t = t-t_pre 
                max_idx = idx  
            elif t-t_pre == max_t and idx < max_idx: 
                max_idx = idx 
            t_pre = t 
        return max_idx 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]) == 1
    # assert s.hardestWorker(70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]) == 12 