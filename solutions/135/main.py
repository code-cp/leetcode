from typing import List 

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyVec = [1] * len(ratings)
        # from start to end, compare left to right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candyVec[i] = candyVec[i-1] + 1
        # from end to start, compare right to left
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candyVec[i] = max(candyVec[i+1] + 1, candyVec[i])
        return sum(candyVec)

if __name__ == "__main__":
    ratings = [1,0,2]
    mySol = Solution()
    assert mySol.candy(ratings) == 5
