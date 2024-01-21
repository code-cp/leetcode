from typing import * 

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        nums1, nums2 = 0, 0 
        
        prev = [0]*2  
        for p in player1:
            if prev[0] == 10 or prev[1] == 10:
                nums1 += p * 2 
            else: 
                nums1 += p 
            prev[0] = prev[1]
            prev[1] = p 
        
        prev = [0]*2  
        for p in player2:
            if prev[0] == 10 or prev[1] == 10:
                nums2 += p * 2 
            else: 
                nums2 += p 
            prev[0] = prev[1]
            prev[1] = p 
            
        if nums1 > nums2: 
            return 1 
        elif nums1 < nums2: 
            return 2 
        else: 
            return 0 
         
            