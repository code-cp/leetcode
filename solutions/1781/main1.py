

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
            freqs = {}
            max_freq = -1 
            for j in range(i, n+1):
                ch_idx = get_idx(s[j-1])
                freq = prefix_sum[ch_idx][j] - prefix_sum[ch_idx][i-1]
                freqs[s[j-1]] = freq 
                # NOTE, max can be calculated normally
                # but min need to update every time 
                max_freq = max(max_freq, freq)
                res += max_freq - min(freqs.values())

        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "aabcbaa"
    assert sol.beautySum(s) == 17 

    s = "aabcb"
    assert sol.beautySum(s) == 5 
