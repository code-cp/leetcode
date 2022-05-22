class Solution:
    def __init__(self):
        self.result = []
        self.path = []
    def backtracking(self, n, k, startId):
        if (len(self.path) == k):
            self.result.append(self.path[:])
            return
        for i in range(startId, n-(k-len(self.path)) + 2): 
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
    def combine(self, n, k):
        self.backtracking(n, k, 1)
        return self.result

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))
