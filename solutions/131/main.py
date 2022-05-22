class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
        
    @staticmethod 
    def isPalindrome(s, start, end): 
        i, j = start, end
        while i < j:
            if s[i] != s[j]: 
                return False 
            i += 1 
            j -= 1 
        return True
            
    def backtracking(self, s, startId): 
        # base case 
        if startId == len(s): 
            self.result.append(self.path[:])
            return 
        for i in range(startId, len(s)): 
            if self.isPalindrome(s, startId, i): 
                self.path.append(s[startId:i+1])
            else: 
                continue 
            self.backtracking(s, i+1)
            self.path.pop()
            
    def partition(self, s):
        self.backtracking(s, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    myStr = "aab"
    print(s.partition(myStr))
