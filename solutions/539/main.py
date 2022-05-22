from typing import List 

class Solution:
    @staticmethod
    def convertStrToTime(strIn):
        result = strIn.split(":")
        timeOut = int(result[0]) * 60 + int(result[1])
        return timeOut
    def findMinDifference(self, timePoints: List[str]) -> int:
        timeList = [self.convertStrToTime(x) for x in timePoints]
        timeList.sort()
        timeList.append(timeList[0] + 24 * 60)
        minDiff = float("inf")
        for i in range(1, len(timeList)):
            diff = timeList[i] - timeList[i-1]
            if diff < minDiff:
                minDiff = diff
        return minDiff

if __name__ == "__main__":
    timePoints = ["23:59","00:00"]
    s = Solution()
    assert s.findMinDifference(timePoints) == 1
