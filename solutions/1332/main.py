class Solution:
    @staticmethod 
    def isPalindrome(s: str) -> bool: 
        i, j = 0, len(s)-1 
        while i < j: 
            if s[i] != s[j]: 
                return False 
            i += 1 
            j -= 1 
        return True  
    def removePalindromeSub(self, s: str) -> int:
        result = 0 
        while not self.isPalindrome(s) and len(s) > 0: 
            s = s.replace("a", "")
            result += 1
        result += 1
        return result

if __name__ == "__main__": 
    s = "baabb"
    sol = Solution()
    assert sol.removePalindromeSub(s) == 2
