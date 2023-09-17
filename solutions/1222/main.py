from typing import * 

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        same_row = list(filter(lambda x: x[0] == king[0], queens))
        same_col = list(filter(lambda x: x[1] == king[1], queens))
        diag1 = list(filter(lambda x: x[0]-x[1] == king[0]-king[1], queens))
        diag2 = list(filter(lambda x: x[0]+x[1] == king[0]+king[1], queens))
        
        same_row.sort(key=lambda x: x[1])
        same_col.sort(key=lambda x: x[0])
        diag1.sort(key=lambda x: x[0])
        diag2.sort(key=lambda x: x[0])
        
        def bsearch(arr, target):
            # find the first position such that target < arr[pos]
            l, r = 0, len(arr)-1 
            while l <= r: 
                mid = (r-l)//2 + l 
                if arr[mid] < target: 
                    l += 1 
                else: 
                    r -= 1 
            return l-1 
        
        ans = []

        idx = bsearch([x[1] for x in same_row], king[1])
        if idx >= 0: 
            ans.append(same_row[idx])
        if idx+1 < len(same_row): 
            ans.append(same_row[idx+1])
            
        idx = bsearch([x[0] for x in same_col], king[0])
        if idx >= 0: 
            ans.append(same_col[idx])
        if idx+1 < len(same_col): 
            ans.append(same_col[idx+1])
            
        idx = bsearch([x[0] for x in diag1], king[0])
        if idx >= 0: 
            ans.append(diag1[idx])
        if idx+1 < len(diag1): 
            ans.append(diag1[idx+1])
            
        idx = bsearch([x[0] for x in diag2], king[0])
        if idx >= 0: 
            ans.append(diag2[idx])
        if idx+1 < len(diag2): 
            ans.append(diag2[idx+1])
            
        return ans 

        
if __name__ == '__main__':
    s = Solution()
    
    # print(s.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]))
    print(s.queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]))