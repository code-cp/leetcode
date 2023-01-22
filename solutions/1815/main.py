from typing import * 

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        n = len(groups)
        count = [0]*batchSize
        for g in groups: 
            count[g%batchSize] += 1 
        state = 0 
        for i in range(1, batchSize): 
            state += count[i] << (i*5)
        
        memo = {}
        def dfs(state, presum, idx):
            res = 0 
            if idx == n: 
                return res
            if memo.get(state, -1) != -1: 
                return memo[state]

            bonus = 1 if (presum%batchSize) == 0 else 0 
            for i in range(batchSize):
                if (state >> (5*i)) % 32 == 0: 
                    continue
                state -= 1 << 5*i 
                res = max(res, dfs(state, (presum+i)%batchSize, idx+1))
                state += 1 << 5*i 
            memo[state] = res + bonus
            return memo[state]

        # count, presum, i
        return count[0] + dfs(state, 0, count[0])

if __name__ == "__main__": 
    s = Solution() 

    batchSize = 3
    groups = [1,2,3,4,5,6]
    assert s.maxHappyGroups(batchSize, groups) == 4 