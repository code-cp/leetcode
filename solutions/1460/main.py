from typing import * 

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # 最小子数组翻转就是冒泡排序
        return sorted(target) == sorted(arr)