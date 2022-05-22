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
            # prune 
            if (candidates[i] > target): 
                return 
            # avoid duplicates 
            if (i > startId and candidates[i] == candidates[i-1]):
                continue 
            self.path.append(candidates[i])
            self.backtracking(candidates, target-candidates[i], i+1)
            self.path.pop()
    
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        self.backtracking(candidates, target, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8 
    result = s.combinationSum2(candidates, target)
    print(result)
