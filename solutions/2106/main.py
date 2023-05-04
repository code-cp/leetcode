from typing import * 

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:        
        n = len(fruits)
        pos = [0]*n 
        presum = [0]*(n+1) 
        for i in range(1,n+1): 
            pos[i-1] = fruits[i-1][0]
            presum[i] = presum[i-1]+fruits[i-1][1]
        
        def lowerBound(pos, target): 
            # find the first element in pos >= target
            l,r = 0,len(pos)-1
            while l<=r: 
                mid=(r-l)//2+l
                if pos[mid]<target:
                    l=mid+1
                else: 
                    r=mid-1
            return l 
        
        res = 0 
        mid = lowerBound(pos,startPos)
        # i marks B, j marks A
        # A----S---B
        for i in range(mid, n):
            dist = pos[i]-startPos
            if dist>k: 
                break 
            d = (k-dist)/2
            j = lowerBound(pos,startPos-d)
            if j>=0 and j<n:
                res = max(res, presum[i+1]-presum[j]) 

        def upperBound(pos, target): 
            # find last element in pos <= target 
            l,r = 0,len(pos)-1
            while l<=r: 
                mid = (r-l)//2+l 
                # NOTE, <= instead of < 
                if pos[mid]<=target: 
                    l=mid+1
                else: 
                    r=mid-1
            # NOTE, return r instead of l 
            # or return l-1 
            return r 

        # i marks B, j marks A
        # B----S---A    
        mid = upperBound(pos,startPos) 
        for i in range(mid, -1, -1): 
            dist = startPos-pos[i]
            if dist > k:  
                break 
            d = (k-dist)/2 
            j = upperBound(pos, startPos+d)
            if j>=0 and j < n: 
                res = max(res, presum[j+1]-presum[i])
                
        return res 
    
if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4) == 9 
    assert s.maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]], 21, 30) == 71 