from typing import * 

class Solution:
    def checkValid(self, pre_sum_T, k, i, j, check_T):
        num_T = pre_sum_T[j] - pre_sum_T[i-1]
        num_F = (j-i+1) - num_T 
        num = num_F if check_T else num_T 
        return num <= k
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        pre_sum_T = [0] * (n+1) 
        for i in range(n): 
            if answerKey[i] == "T": 
                pre_sum_T[i+1] = pre_sum_T[i] + 1
            else: 
                pre_sum_T[i+1] = pre_sum_T[i]
        max_len = 0 
        left, right = 1, n 
        while left <= right: 
            valid = False 
            mid = left + (right - left) // 2 
            for start in range(n-mid+1):
                # end - start + 1 = mid 
                end = mid + start - 1 
                if (self.checkValid(pre_sum_T, k, start+1, end+1, True) or 
                    self.checkValid(pre_sum_T, k, start+1, end+1, False)):  
                    valid = True 
                    break 
            if valid: 
                max_len = max(max_len, mid)
                left = mid + 1 
            else: 
                right = mid - 1 
        return max_len

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