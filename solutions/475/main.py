from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)

        radius = 0
        heaterId = 0
        for i in range(len(houses)):
            # skip houses at same position
            if i != 0 and houses[i] == houses[i-1]:
                continue
            curDiff = abs(houses[i] - heaters[heaterId])
            while heaterId+1 < len(heaters) and abs(houses[i] - heaters[heaterId+1]) < curDiff:
                curDiff = abs(houses[i] - heaters[heaterId+1])
                heaterId += 1
                # skip heaters at same position
                while heaterId+1 < len(heaters) and heaters[heaterId] == heaters[heaterId+1]:
                    heaterId = heaterId+1
            if curDiff > radius:
                radius = curDiff
        return radius

if __name__ == "__main__": 
    houses = [1,2,3]
    heaters = [2]
    s = Solution()
    assert s.findRadius(houses, heaters) == 1
