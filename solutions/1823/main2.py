from typing import * 

from collections import deque 
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque([i for i in range(1, n + 1)]) 
        while len(friends) > 1:
            for _ in range(k-1):
                friends.append(friends.popleft()) 
            friends.popleft()
        return friends[0]

if __name__ == "__main__": 
    s = Solution() 

    n = 5
    k = 2
    result = s.findTheWinner(n, k) 
    assert result == 3 