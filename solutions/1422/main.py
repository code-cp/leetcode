class Solution:
    def maxScore(self, s: str) -> int:
        presum = [0] * len(s)
        count_one = 0 
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                count_one += 1 
            presum[i] = count_one
        count_zero = 0 
        max_score = 0 
        for i in range(len(s)-1):
            if s[i] == "0":
                count_zero += 1 
            cur_score = presum[i+1] + count_zero
            max_score = max(max_score, cur_score)
        if len(s) > 1 and s[-1] == "1":
            max_score = max(max_score, count_zero+1)
        return max_score

if __name__ == "__main__": 
    sol = Solution()

    s = "1111"
    assert sol.maxScore(s) == 3 

    s = "011101"
    assert sol.maxScore(s) == 5 

    s = "00111"
    assert sol.maxScore(s) == 5