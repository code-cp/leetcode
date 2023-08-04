from typing import * 
import heapq 
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # 假设找的是正面的最小值
        
        ans = 0 
        cards = []
        seen = set() 
        
        for (f, b) in zip(fronts, backs):
            # 正反面相同的一定不是答案
            if f == b:
                seen.add(f)
                continue 
            # 假设最小值是正面
            cards.append((min(f, b), max(f, b)))
        heapq.heapify(cards)

        while len(cards) > 0: 
            (f, b) = heapq.heappop(cards) 
            # 如果最小值没见过，那就是答案
            if f not in seen: 
                return f 
            if b not in seen: 
                # 如果最小值见过了，把b的值作为正面
                seen.add(f)
                heapq.heappush(cards, (b, f))    
        
        return ans 
            
if __name__ == "__main__": 
    s = Solution()
    
    assert s.flipgame([2,1,1,2,2], [2,2,1,2,1]) == 0 