class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        # dp[0][x] is 010101...
        # dp[1][x] is 101010...
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = 1 if s[0] == "1" else 0 
        dp[1][0] = 1 if s[0] == "0" else 0 

        for i in range(1, n):
            if i % 2 == 0:  
                dp[int(s[i])][i] = dp[int(s[i])][i-1]
                dp[1-int(s[i])][i] = dp[1-int(s[i])][i-1]+1
            else: 
                dp[int(s[i])][i] = dp[int(s[i])][i-1]+1
                dp[1-int(s[i])][i] = dp[1-int(s[i])][i-1]

        return min(dp[0][-1], dp[1][-1])

if __name__ == "__main__": 
    sol = Solution() 

    s = "10"
    assert sol.minOperations(s) == 0

    s = "0100"
    assert sol.minOperations(s) == 1 