from typing import List 

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp table
        n = len(questions)
        dp = [0] * (n+1)
        # initialize
        dp[n-1] = questions[-1][0]
        # traverse
        for i in range(n-2, -1, -1):
            # skip
            skip = dp[i+1]
            # solve
            solve = questions[i][0] + dp[min(n, i+questions[i][1]+1)]
            dp[i] = max(skip, solve)
        return dp[0]

if __name__ == "__main__":
    questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    s = Solution()
    assert s.mostPoints(questions) == 7
