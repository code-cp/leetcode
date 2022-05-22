class Solution:
    def __init__(self): 
        self.path = ""
        self.result = []
        
        self.letterMap = {
            "2" : 'abc', 
            "3" : 'def', 
            "4" : 'ghi', 
            "5" : 'jkl', 
            "6" : 'mno', 
            "7" : 'pqrs', 
            "8" : 'tuv', 
            "9" : 'wxyz'
        }
    
    def backtracking(self, digits, startId): 
        if (startId == len(digits)):
            self.result.append(self.path)
            return 
        digit = digits[startId]
        letters = self.letterMap[digit] 
        for i in range(0, len(letters)):
            self.path += letters[i]
            self.backtracking(digits, startId+1)
            self.path = self.path[:-1]
        
    def letterCombinations(self, digits):
        if (len(digits) == 0): 
            return self.result
        self.backtracking(digits, 0) 
        return self.result

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
