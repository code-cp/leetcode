from typing import * 

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time2num(event):
            e = event.split(":")
            t = int(e[0])*60 + int(e[1])
            return t 
        
        s1,e1 = time2num(event1[0]), time2num(event1[1])
        s2,e2 = time2num(event2[0]), time2num(event2[1])
        
        if max(s1,s2)<=min(e1,e2): 
            return True 
        return False 
        