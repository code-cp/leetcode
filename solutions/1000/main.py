from typing import * 

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        # 每次合并消去(k-1)个数
        # 最后剩下1个数
        # 相当于一共消去n-1个数
        if (n-1)%(k-1) != 0:
            return -1 
        
        # 前缀和
        # prefix[i]指的是下标[0,i)的和
        prefix = [0]*(n+1)
        for i in range(n): 
            prefix[i+1] = prefix[i]+stones[i]
            
        # dp[i][j]表示最小成本
        # 成本指的是合并stones[i]~stones[j]得到(j-i)%(K-1)+1堆石头  
        dp = [[float("inf")]*n for _ in range(n)]
        
        # init 
        for i in range(n):
            # 把一个数merge为一堆，cost = 0
            # 因为初始状态就是单独一个个数
            dp[i][i] = 0 
        
        # 必须先遍历长度，因为l比较大的时候的状态是用l比较小的时候的状态推出来的
        # 不可以用for i....for j...直接遍历左右端点
        # eg 计算dp[i][j]的时候，必须保证dp[m+1][j]已经计算出来了 
        for l in range(2, n+1):
            # l是subarray长度
            for i in range(n-l+1):
                # i是起始位置，j是结束位置
                j = i+l-1 
                for m in range(i, j, k-1):
                    # m是分割点
                    # 注意, m+=K-1而不是m+=1，因为要保证[i,m]可以分割为一堆
                    # [i,m]分割为1堆，[m+1,j]分割为几堆是确定的，所以不需要额外记录几堆的状态
                    dp[i][j] = min(dp[i][j], dp[i][m]+dp[m+1][j])
                # 如果当前长度可以合并，总的cost跟合并顺序无关，
                # ie每次合并，无论是第几层，增加的成本都是[i,j]的和
                if (l-1)%(k-1) == 0:
                    # [0,j+1) - [0,i) = [i,j+1) = [i,j]
                    dp[i][j] += prefix[j+1]-prefix[i]
                    
        return dp[0][n-1]
                    
        
if __name__ == "__main__": 
    s = Solution() 
    
    stones = [3,2,4,1]
    k = 2
    assert s.mergeStones(stones, k) == 20 