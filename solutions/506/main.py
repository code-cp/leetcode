from typing import List 
import heapq 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)
        pq = []
        for i in range(len(score)):
            heapq.heappush(pq, (-score[i], i))
        for i in range(len(score)):
            athlete_score, athlete_id = heapq.heappop(pq)
            if i == 0:
                result[athlete_id] = "Gold Medal"
            elif i == 1:
                result[athlete_id] = "Silver Medal"
            elif i == 2:
                result[athlete_id] = "Bronze Medal"
            else:
                result[athlete_id] = str(i+1)
        return result

if __name__ == "__main__": 
    score = [5,4,3,2,1]
    ans = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    s = Solution()
    assert s.findRelativeRanks(score) == ans 
