from typing import * 

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt = 1 
        visited = [0]*n 
        visited[0] = 1 
        
        i = 0 
        while True: 
            i = (i+cnt*k)%n 
            if visited[i] == 1:
                break 
            visited[i] = 1    
            cnt += 1 
            
        ans = [i+1 for i, x in enumerate(visited) if x == 0]
        
        return ans  

if __name__ == '__main__': 
    s = Solution()
    
    assert s.circularGameLosers(5, 2) == [4, 5]