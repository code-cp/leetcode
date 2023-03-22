from typing import * 

# https://leetcode.cn/problems/best-team-with-no-conflicts/discussion/comments/1964431
# 首先对数组进行排序，先按年龄升序，如果年龄相同，再按分数升序。（可以构造一个下标数组）
# 设dp[i]为在球员1~i中选出i所能获得的最大分数。状态转移方程如下： dp[i]=max{dp[j]}+score[i]（dp[j]代表序列与i不冲突）
# 考虑不冲突的限制：由于是按年龄升序的，这意味着如果要选出球员i，要求scores[i]不小于前面选出的每一个。
# 而这个约束并不需要刻意维护前面序列的最大值，因为scores[j]同样要不小于前面的每一个，所以只要scores[i]>scores[j]
# PS:为什么所以年龄相同时，要按分数升序排列？可以考虑如下例子：
# (1,3)与(1,2)显然是不冲突的，但如果(1,3)排在前，则不可能同时选出这两个球员，因而会出错

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort(key=lambda x: (x[0], x[1]))
        n = len(scores)
        dp = [0]*n
        # NOTE, set init value to each score, cannot be 0 
        for i in range(n):
            dp[i] = players[i][1]
        for i in range(1, n): 
            for j in range(i): 
                if players[i][1] >= players[j][1]: 
                    dp[i] = max(dp[i], dp[j]+players[i][1])  
        # NOTE, take max, cannot return dp[-1]
        return max(dp)
    
if __name__ == "__main__": 
    s = Solution() 

    scores = [9,2,8,8,2]
    ages = [4,1,3,3,5]
    assert s.bestTeamScore(scores, ages) == 27 

    # scores = [1,2,3,5]
    # ages = [8,9,10,1]
    # assert s.bestTeamScore(scores, ages) == 6 
    
    # scores = [4,5,6,5]
    # ages = [2,1,2,1]
    # assert s.bestTeamScore(scores, ages) == 16 