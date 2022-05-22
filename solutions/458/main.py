from typing import List 
import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # note, NOT minutesToTest // minutesToDie
        # also, smallest base is 2, not 1
        base = minutesToTest // minutesToDie + 1
        num = math.ceil(math.log(buckets, base))
        return num

if __name__ == "__main__":
    buckets = 1000 
    minutesToDie = 15 
    minutesToTest = 60
    s = Solution()
    assert s.poorPigs(buckets, minutesToDie, minutesToTest) == 5
