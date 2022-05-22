class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    def backtracking(self, k, n, startId): 
        if (n < 0): 
            return 
        if (k == 0):
            if (n == 0):
                # note here is self.path[:]
                self.result.append(self.path[:])
            return 
        # note here is 9 - k + 2, not 9 - (k - path.size()) + 2
        for i in range(startId, 9-k+2):
            self.path.append(i)
            self.backtracking(k-1, n-i, i+1)
            self.path.pop()
    def combinationSum3(self, k, n):
        self.backtracking(k, n, 1)
        return self.result 

if __name__ == "__main__":
    k, n = 3, 7
    s = Solution()
    print(f"result is {s.combinationSum3(k, n)}")
