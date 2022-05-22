from typing import List 

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalSum = 0
        curSum = 0
        result = 0
        for i in range(len(cost)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                result = i + 1
        if totalSum < 0:
            return -1
        return result

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    mySol = Solution()
    assert mySol.canCompleteCircuit(gas, cost) == 3
