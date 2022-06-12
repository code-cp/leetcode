from typing import * 

# TLE 
class Solution:
    def backtracking(self, cookies, k, target, i): 
        if i == len(cookies):
            gap = max(self.assign) - min(self.assign)
            if gap < self.min_gap:
                self.min_gap = gap 
                self.max_total = max(self.assign)
            return 

        add = cookies[i] 
        skip_check = False 
        if add + min(self.assign) > target: 
            skip_check = True  

        for j in range(k):
            # if skip_check or self.assign[j] + add <= target: 
            self.assign[j] += add 
            self.backtracking(cookies, k, target, i+1)
            self.assign[j] -= add 

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.max_total = 0 
        self.min_gap = float("inf")
        self.assign = [0] * k 

        target = sum(cookies) / k
        cookies = sorted(cookies, reverse=True) 
        self.backtracking(cookies, k, target, 0)
        return self.max_total

if __name__ == "__main__": 
    s = Solution() 

    cookies = [8,15,10,20,8]
    k = 2
    assert s.distributeCookies(cookies, k) == 31

    cookies = [6,1,3,2,2,4,1,2]
    k = 3 
    assert s.distributeCookies(cookies, k) == 7

    cookies = [76265,7826,16834,63341,68901,58882,50651,75609]
    k = 8
    print(s.distributeCookies(cookies, k))

    cookies = [15,14,8,13,7,2,13,19]
    k = 3
    assert s.distributeCookies(cookies, k) == 32