class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        startTime.sort()
        endTime.sort()
        # ref https://stackoverflow.com/a/20297273/8519188
        return bisect_right(startTime, queryTime) - bisect_left(endTime, queryTime)

