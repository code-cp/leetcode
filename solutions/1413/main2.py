from typing import * 

from itertools import accumulate
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(-min(accumulate(nums)), 0) + 1