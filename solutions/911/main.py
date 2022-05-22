from typing import List 

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.totalVoteMap = {}
        self.latestVoteMap = {}
        self.result = []
        self.times = times
        for i in range(len(times)):
            # 计数
            if persons[i] not in self.totalVoteMap:
                self.totalVoteMap[persons[i]] = 0
            if persons[i] not in self.latestVoteMap:
                self.latestVoteMap[persons[i]] = 0
            self.totalVoteMap[persons[i]] += 1
            self.latestVoteMap[persons[i]] = times[i]
            # 唱票
            mvp, mv = 0, -float("inf")
            for p, v in self.totalVoteMap.items():
                if v > mv:
                    mvp = p
                    mv = v
                elif v == mv:
                    # 处理平局
                    if self.latestVoteMap[p] > self.latestVoteMap[mvp]:
                        mvp = p
            self.result.append(mvp)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if self.times[mid] > t:
                right = mid - 1
            elif self.times[mid] < t:
                left = mid + 1
            else:
                return self.result[mid]
        if self.times[mid] > t:
            mid -= 1
        return self.result[mid]

if __name__ == "__main__": 
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    obj = TopVotedCandidate(persons, times)
    queries = [3, 12, 25, 15, 24, 8]
    ans = [0, 1, 1, 0, 0, 1]
    for i in range(len(queries)): 
        assert obj.q(queries[i]) == ans[i] 
