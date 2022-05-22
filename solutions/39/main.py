class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    def backtracking(self, candidates, target, startId): 
        # prune 
        if (target < 0): 
            return 
        # base case 
        if (target == 0): 
            self.result.append(self.path[:])
            return 
        for i in range(startId, len(candidates)):
            if (candidates[i] > target):
                return 
            self.path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i)
            self.path.pop()
            
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        self.backtracking(candidates, target, 0)
        return self.result

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))
