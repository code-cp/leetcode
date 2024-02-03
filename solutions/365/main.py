from typing import * 

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # 这一题可以直接用裴蜀定理解决，裴蜀定理用于判断是否存在整数解，对于水壶问题，就有下面的方程：jug1Capacity x+jug2Capacity y = targetCapacity，根据这个方程，实际上可以发现，仅当targetCapacity是二者最大公约数的倍数的时候，方程才有整数解，所以进行如下分析：
        # 首先边界分析，如果目标大于壶1加上壶2总容量则必然不可能得出结果，然后根据定理，目标对壶1和壶2目前容量的最大公约数取模如果等于0，则说明可以完成分配，反之则不能。
        
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False 
        
        def gcd(a, b):
            if b == 0:
                return a 
            return gcd(b, a%b)
        
        g = gcd(jug1Capacity, jug2Capacity)
        if targetCapacity % g == 0: 
            return True
        else:
            return False 