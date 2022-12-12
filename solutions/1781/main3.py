# TLE 
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        get_idx = lambda ch: ord(ch)-ord("a")
        # NOTE, index starts at 1 to simply 
        prefix_sum = [[0 for _ in range(n+1)] for _ in range(26)]

        for i in range(n): 
            for j in range(26): 
                if j == get_idx(s[i]):
                    prefix_sum[j][i+1] = prefix_sum[j][i]+1
                else: 
                    prefix_sum[j][i+1] = prefix_sum[j][i]
            
        res = 0 
        for i in range(1, n+1): 
            # skip array with len=2 
            for j in range(i+2, n+1): 
                max_f = -1 
                min_f = float("inf")
                for ch in set(s[i-1:j]):
                    ch_idx = get_idx(ch)
                    freq = prefix_sum[ch_idx][j] - prefix_sum[ch_idx][i-1]
                    max_f = max(max_f, freq)
                    min_f = min(min_f, freq)
                res += max_f - min_f 

        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "aabcbaa"
    assert sol.beautySum(s) == 17 

    s = "aabcb"
    assert sol.beautySum(s) == 5 
