from typing import * 

class Solution:
    def backtracking(self, n, requests, result, res_idx): 
        # update result 
        if all(b == 0 for b in self.buildings): 
            self.max_req = max(result, self.max_req)

        # base case 
        if res_idx == len(requests):
            return 
        
        for i in range(res_idx, len(requests)): 
            self.buildings[requests[i][0]] -= 1 
            self.buildings[requests[i][1]] += 1 
            self.backtracking(n, requests, result+1, i+1)
            self.buildings[requests[i][0]] += 1 
            self.buildings[requests[i][1]] -= 1 


    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.buildings = [0] * n 
        self.max_req = 0 
        self.backtracking(n, requests, 0, 0)
        return self.max_req

if __name__ == "__main__": 
    s = Solution()

    n = 2
    requests = [[0,1],[1,0]]
    result = s.maximumRequests(n, requests)
    assert result == 2

    n = 3
    requests = [[0,0],[1,2],[2,1]]
    result = s.maximumRequests(n, requests)
    assert result == 3

    n = 5
    requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
    result = s.maximumRequests(n, requests)
    assert result == 5 

    n = 3
    requests = [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]]
    result = s.maximumRequests(n, requests)
    assert result == 4