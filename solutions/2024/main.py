from typing import * 

class Solution:
    def slidingWin(self, ans, k, key):
        max_len = 0 
        curr_len = 0 
        count = 0 
        start = 0 
        for i in range(len(ans)): 
            if ans[i] == key:
                curr_len += 1
                continue  
            count += 1 
            if count > k:
                max_len = max(max_len, curr_len)
                while start < len(ans) and count > k:
                    if ans[start] != key: 
                        count -= 1 
                    start += 1 
                    curr_len -= 1 
            curr_len += 1
        max_len = max(max_len, curr_len)
        return max_len  
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        key = "T" 
        len1 = self.slidingWin(answerKey, k, key) 
        key = "F" 
        len2 = self.slidingWin(answerKey, k, key) 
        return max(len1, len2)

if __name__ == "__main__":
    s = Solution()

    answerKey = "TTFF"
    k = 2
    assert s.maxConsecutiveAnswers(answerKey, k) == 4

    answerKey = "TTFTTFTT"
    k = 1
    assert s.maxConsecutiveAnswers(answerKey, k) == 5

    answerKey = "TTFTTTTTFT"
    k = 1
    assert s.maxConsecutiveAnswers(answerKey, k) == 8