class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: 
            return 1 
        next_reminder = lambda prev, k: (prev*10+1)%k   
        num = 1
        prev = 1  
        for _ in range(k): 
            num += 1 
            prev = next_reminder(prev, k)
            if prev == 0: 
                return num 
        return -1 