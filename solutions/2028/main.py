from typing import * 

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m+n)
        n_sum = total - sum(rolls) 
        if n_sum <= 0: 
            return [] 
        if n_sum / n > 6: 
            return []
        avg = n_sum // n
        res = [] 
        while n_sum > 0:
            if avg == 0 or avg > 6: 
                return []
            if n_sum > avg * (n-len(res)): 
                avg += 1 
                res.append(avg)
                n_sum -= avg
            elif n_sum < avg * (n-len(res)): 
                avg -= 1 
                res.append(avg)
                n_sum -= avg
            else: 
                res.append(avg)
                n_sum -= avg
        return res  

if __name__ == "__main__": 
    s = Solution()

    rolls = [3,2,4,3]
    mean = 4
    n = 2
    result = s.missingRolls(rolls, mean, n)
    assert result == [6, 6]

    rolls = [1,5,6]
    mean = 3
    n = 4
    result = s.missingRolls(rolls, mean, n)
    assert result == [3,2,2,2]

    rolls = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3]
    mean = 2
    n = 53
    result = s.missingRolls(rolls, mean, n) 
    assert result == []