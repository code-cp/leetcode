
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = [0] * 26 
        front = [[0 for _ in range(n)] for _ in range(26)]
        front[ord(s[0])-ord("a")][0] = 1 
        total[ord(s[0])-ord("a")] = 1
        back = [[0 for _ in range(n)] for _ in range(26)]
        back[ord(s[-1])-ord("a")][-1] = 1

        for i in range(1, n): 
            total[ord(s[i])-ord("a")] += 1 
            for j in range(26): 
                if j == ord(s[i])-ord("a"):
                    front[j][i] = front[j][i-1]+1
                else: 
                    front[j][i] = front[j][i-1]
        for i in range(n-2, -1, -1): 
            for j in range(26): 
                if j == ord(s[i])-ord("a"):
                    # index starts with 1 
                    back[j][i] = back[j][i+1]+1
                else: 
                    back[j][i] = back[j][i+1]
            

        res = 0 
        for i in range(n): 
            freqs = {}
            max_f = -1 
            for j in range(i, n): 
                ch = s[j]
                if i == 0 and j != n-1: 
                    freq = total[ord(ch)-ord("a")] - back[ord(ch)-ord("a")][j+1]
                elif i == 0 and j == n-1: 
                    freq = total[ord(ch)-ord("a")]
                elif j == n-1: 
                    freq = total[ord(ch)-ord("a")] - front[ord(ch)-ord("a")][i-1] 
                else: 
                    freq = total[ord(ch)-ord("a")] - front[ord(ch)-ord("a")][i-1] - back[ord(ch)-ord("a")][j+1]

                freqs[ord(ch)-ord("a")] = freq 
                max_f = max(max_f, freq)
                
                res += max_f - min(freqs.values()) 

        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "aabcbaa"
    assert sol.beautySum(s) == 17 

    s = "aabcb"
    assert sol.beautySum(s) == 5 
