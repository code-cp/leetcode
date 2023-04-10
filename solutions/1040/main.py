from typing import * 

# https://leetcode.cn/problems/moving-stones-until-consecutive-ii/solutions/5446/jie-ti-si-lu-by-owenzzz/
# https://leetcode.cn/problems/moving-stones-until-consecutive-ii/solutions/2212638/tu-jie-xia-tiao-qi-pythonjavacgo-by-endl-r1eb/

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()
        
        # upper bound 
        max_move = max(stones[-1] - stones[1] + 1 - (n - 1), stones[-2] - stones[0] + 1 - (n - 1))
        
        # lower bound 
        min_move = max_move  
        # 如果最后游戏结束，那么一定有 n 个连续坐标摆满了石子。如果我们要移动最少，必定要找一个石子序列，
        # 使得在 n 大小连续的坐标内，初始时有最多的石子
        left = 0
        for right in range(n): 
            while stones[right] - stones[left] + 1 > n: 
                # window is too long 
                left += 1 
            if stones[right] - stones[left] + 1 == n - 1 and right - left + 1 == n - 1:
                # eg 123xxxx4, min move is 2 
                # since we cannot move to 1234, because 4 is still end stone 
                # we can only do 23x1xx4, then 2341  
                min_move = min(min_move, 2) 
            else: 
                # 选择包含石子最多的窗口
                # right - left + 1 means how many stones are already in window 
                # note that left, right are indices of stones 
                # remaining step is to move all stones outside of window to be inside window 
                # eg [4,7,9], i = 1, j = 2
                min_move = min(min_move, n - (right - left + 1))
        
        return [min_move, max_move]
                 
                    
        
if __name__ == "__main__": 
    s = Solution() 

    assert s.numMovesStonesII([6,5,4,3,10]) == [2,3]   
    # assert s.numMovesStonesII([7,4,9]) == [1,2]