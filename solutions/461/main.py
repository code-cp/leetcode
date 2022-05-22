from typing import List 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        while z != 0:
            z &= (z-1)
            count += 1
        return count

if __name__ == "__main__":
    x, y = 1, 4 
    s = Solution()
    assert s.hammingDistance(x, y) == 2
