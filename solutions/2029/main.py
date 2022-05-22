from typing import List 

class Solution:
    def backtracking(self, count, person, total): 
        # base case 
        if person == 0 and total != 0 and total % 3 == 0: 
            # Alice wins 
            return True 
        if sum(count) == 0: 
            # Bob wins 
            return False 

        backtrack = False 
        for i in range(0, 3): 
            # pruning 
            if (total+i) % 3 == 0: 
                continue 
            if count[i] == 0: 
                continue 
            if total % 3 != 0 and count[0] > 0 and i != 0: 
                continue 

            # backtracking 
            backtrack = True 
            count[i] -= 1 
            if self.backtracking(count, 1-person, total+i):
                return True 
            count[i] += 1

        if person == 0: 
            # Bob wins 
            return False 
        elif not backtrack: 
            # Alice wins 
            return True   
        else:   
            # Bob wins 
            return False 

    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0] * 3 
        for s in stones: 
            count[s%3] += 1 
        # person 0 = Alice 
        # person 1 = Bob 
        return self.backtracking(count, 0, 0)

if __name__ == "__main__": 
    stones = [5,1,2,4,3]
    s = Solution()
    assert not s.stoneGameIX(stones)