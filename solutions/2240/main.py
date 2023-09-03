class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0 
        n = total // cost1 
        for i in range(n+1): 
            ans += (total - i*cost1) // cost2 + 1
        return ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.waysToBuyPensPencils(total=20, cost1=10, cost2=5) == 9