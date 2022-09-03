from typing import * 
# dp
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        # 定义 \textit{dp}[i]dp[i] 为以 \textit{pairs}[i]pairs[i] 为结尾的最长数对链的长度
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i): 
                if pairs[i][0] > pairs[j][1]: 
                    dp[i] = max(dp[i], dp[j]+1)
        # 最长数对肯定包含最后一个数
        return dp[-1] 

if __name__ == "__main__": 
    s = Solution()

    pairs = [[1,2],[2,3],[3,4]]
    assert s.findLongestChain(pairs) == 2 

    # pairs = [[1,2],[7,8],[4,5]]
    # assert s.findLongestChain(pairs) == 3 