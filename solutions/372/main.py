from typing import List 

# ref
# https://www.geeksforgeeks.org/multiply-large-integers-under-large-modulo/
# https://www.geeksforgeeks.org/modulo-1097-1000000007/
# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
# https://youtu.be/8bWdMellTmU
class Solution:
    def __init__(self):
        self.m = 1337

    # time complexity O(logb)
    # space complexity O(1)
    def quickPowMod(self, a, b):
        a %= self.m
        if a == 0:
            return 0
        result = 1
        while b > 0:
            if b & 1:
                result = (result * a) % self.m
            b = b >> 1
            a = (a**2) % self.m
        return result

    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        for i in range(len(b)-1, -1, -1):
            result = (result * self.quickPowMod(a, b[i])) % self.m
            a = self.quickPowMod(a, 10)
        return result

if __name__ == "__main__": 
    a = 2147483647 
    b = [2,0,0]
    s = Solution()
    assert s.superPow(a, b) == 1198
