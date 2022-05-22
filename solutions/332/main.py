from typing import List 
from collections import defaultdict 

class Solution:
    def __init__(self):
        self.result = []
        self.targets = defaultdict(list)
    def backtracking(self, tickets):
        # base case
        if len(self.result) == len(tickets)+1:
            return True
        start = self.result[-1]
        # NOTE, need to sort here
        self.targets[start].sort()
        for _ in self.targets[start]:
            dest = self.targets[start].pop(0)
            self.result.append(dest)
            if self.backtracking(tickets):
                return True
            self.result.pop()
            self.targets[start].append(dest)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # targets {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        for item in tickets:
            self.targets[item[0]].append(item[1])
        self.result.append("JFK")
        self.backtracking(tickets)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(s.findItinerary(tickets))
