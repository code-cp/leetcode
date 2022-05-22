from typing import List 

class Solution:
    def integerReplacement(self, n: int) -> int:
        # base case
        if n == 1:
            return 0

        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1 + min(self.integerReplacement(n-1), self.integerReplacement(n+1))

if __name__ == "__main__":
    s = Solution()
    assert s.integerReplacement(8) == 3
