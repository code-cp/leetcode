class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        cnt = {} 
        nums = [0] * n
        j = -1 
        for i in range(n): 
            cnt[s[i]] = cnt.get(s[i], 0) + 1 
            nums[i] = cnt[s[i]]
            nums[i] -= n//4 
            if j == -1 and nums[i] > 0:
                j = i
        k = j  
        for i in range(j+1, n): 
            if nums[i] > 0: 
                k = i 
        if j == -1: 
            return 0
        return k-j+1

if __name__ == "__main__": 
    sol = Solution() 

    s = "WWQQRRRRQRQQ"
    assert sol.balancedString(s) == 4 

    # s = "QWER"
    # assert sol.balancedString(s) == 0

    # s = "QQWE"
    # assert sol.balancedString(s) == 1 