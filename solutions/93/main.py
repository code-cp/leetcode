class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    @staticmethod 
    def isValid(s, start, end): 
        if start > end: 
            return False 
        if s[start] == '0' and start != end: 
            return False 
        num = 0
        for i in range(start, end+1):
            if s[i] > '9' or s[i] < '0':
                return False 
            n = int(s[i])
            num = num*10 + n 
            if num > 255: 
                return False 
        return True 
    def backtracking(self, s, startId): 
        # base case 
        if len(self.path) == 4 and startId == len(s):
            self.result.append(".".join(self.path[:]))
            return 
        for i in range(startId, len(s)):
            if self.isValid(s, startId, i): 
                self.path.append(s[startId:i+1])
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                break 
    def restoreIpAddresses(self, s):
        if len(s) > 12:
            return self.result 
        self.backtracking(s, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    myStr = "25525511135"
    print(s.restoreIpAddresses(myStr))
