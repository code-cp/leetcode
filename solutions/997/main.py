from typing import List 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # handle one person case
        if n == 1 and len(trust) == 0:
            return 1
        # find town judge
        vote = [0] * (n+1)
        for t in trust:
            vote[t[1]] += 1
        maxVote = max(vote)
        if maxVote != n-1:
            return -1
        tj = vote.index(maxVote)
        for t in trust:
            if tj == t[0]:
                return -1
        return tj

if __name__ == "__main__": 
    n = 3 
    trust = [[1,3],[2,3]]
    s = Solution()
    assert s.findJudge(n, trust) == 3
