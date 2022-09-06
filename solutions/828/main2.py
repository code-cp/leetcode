class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = [0] * len(s)
        total = 0 
        last0, last1 = {}, {}
        for i, c in enumerate(s): 
            # total records the number of substrings end at i 
            total += (i - last0.get(c, -1)) - (last0.get(c, -1) - last1.get(c, -1))
            dp[i] = total
            last1[c] = last0.get(c, -1)
            last0[c] = i 
        return sum(dp) 



if __name__ == "__main__": 
    s = Solution()

    input_str = "ABC"
    assert s.uniqueLetterString(input_str) == 10 