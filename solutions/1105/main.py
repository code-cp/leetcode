from typing import * 

# ref https://leetcode.cn/problems/filling-bookcase-shelves/solutions/2240688/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-0vg6/

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float("inf")]*n 
        dp = [0]+dp 
        
        for i in range(n): 
            max_height, width_left = 0, shelfWidth 
            for j in range(i,-1,-1): 
                width_left -= books[j][0]
                if width_left < 0:
                    # not enough space 
                    break 
                # [0,j] books are already placed 
                # need to put [j+1,i] books
                # the height is the max. of [j+1,i] books
                # j is determined until [j+1,i] reaches max. width  
                max_height = max(max_height, books[j][1])
                dp[i+1] = min(dp[i+1], dp[j]+max_height)
        
        return dp[-1]
    
if __name__ == "__main__": 
    s = Solution() 
   
    books = [[1,3],[2,4],[3,2]]
    shelfWidth = 6
    assert s.minHeightShelves(books, shelfWidth) == 4 
    
    # books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    # shelfWidth = 4
    # assert s.minHeightShelves(books, shelfWidth) == 6 