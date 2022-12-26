class Solution:
    def countHomogenous(self, s: str) -> int:
        M = 10**9+7
        res = 0
        cur = s[0]
        cnt = 1  
        for i in range(1, len(s)): 
            if s[i] == cur: 
                cnt += 1 
            else: 
                res += ((1+cnt)*cnt//2)%M
                res %= M 
                cur = s[i]
                cnt = 1 
        res += ((1+cnt)*cnt//2)%M
        res %= M 
        return int(res)

if __name__ == "__main__": 
    sol = Solution() 

    s = "abbcccaa"
    assert sol.countHomogenous(s) == 13 