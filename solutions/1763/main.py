class Solution:
    def isNice(self, s: str) -> bool: 
        for i in range(len(s)): 
            if s[i].lower() not in s or s[i].upper() not in s: 
                return False 
        return True 
    def longestNiceSubstring(self, s: str) -> str:
        max_pos, max_len = 0, 0
        for i in range(len(s)): 
            for j in range(i+1, len(s)): 
                if self.isNice(s[i:j+1]): 
                    if max_len < j-i+1: 
                        max_len = j-i+1 
                        max_pos = i
        return s[max_pos:max_pos+max_len]

if __name__ == "__main__": 
    s = "YazaAay"
    sol = Solution()
    assert sol.longestNiceSubstring(s) == "aAa"