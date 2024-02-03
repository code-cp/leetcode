from typing import * 

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def costOfAlloy(machine_index, alloy_num): 
            nonlocal composition
            nonlocal cost 
            nonlocal stock 
            
            machine = composition[machine_index]
            total_cost = 0 
            for i, s in enumerate(stock): 
                total_cost += max(0, alloy_num * machine[i] - s) * cost[i]
                
            return total_cost 
                
        def bsearch(machine_index):
            nonlocal budget 
        
            max_num = (budget + max(stock)) // min(composition[machine_index])
            
            l, r = 0, max_num 
            while l <= r: 
                mid = (r-l) // 2 + l 
                if costOfAlloy(machine_index, mid) <= budget:
                    l = mid + 1 
                else: 
                    r = mid - 1 
            
            return l-1 
        
        nums = [0]*k 
        for i in range(k): 
            nums[i] = bsearch(i)
            
        return int(max(nums))
    
if __name__ == '__main__':
    s = Solution()
    
    n = 3
    k = 2
    budget = 15
    composition = [[1,1,1],[1,1,10]]
    stock = [0,0,0]
    cost = [1,2,3]
    assert s.maxNumberOfAlloys(n, k, budget, composition, stock, cost) == 2