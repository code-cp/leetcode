# ref https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/solutions/2221544/tu-jie-tan-xin-zuo-fa-yi-tu-miao-dong-py-huik/

class Solution:
    def longestDecomposition(self, text: str) -> int:
        # base case 
        if text == "": 
            return 0 
        for i in range(1, len(text)//2+1):
            if text[:i] == text[-i:]:
                return 2+self.longestDecomposition(text[i:-i])
        return 1         