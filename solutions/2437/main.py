class Solution:
    def countTime(self, time: str) -> int:
        ans = 1 
        if time[0] == "?":
            if time[1] == "?": 
                ans *= 24 
            elif int(time[1]) > 3: 
                ans *= 2 
            else: 
                ans *= 3 
        if time[1] == "?": 
            if time[0] == "?":
                # already calculated  
                ans *= 1 
            elif int(time[0]) < 2: 
                ans *= 10 
            else: 
                ans *= 4 
        # time[2] is ":"
        if time[3] == "?": 
            ans *= 6 
        if time[4] == "?": 
            ans *= 10 
        return ans 

if __name__ == "__main__": 
    s = Solution() 
    
    assert s.countTime("0?:0?") == 100 