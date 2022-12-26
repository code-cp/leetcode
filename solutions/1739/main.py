import math 
class Solution:
    def minimumBoxes(self, n: int) -> int:
        def numBoxes(area): 
            d = int(math.sqrt(2*area))
            while (d+1)*d/2 > area: 
                d -= 1 
            diff = int(area-(d+1)*d/2) 
            arr = [0]*d
            for i in range(d): 
                arr[i] = d-i 
            for i in range(diff): 
                arr[i] += 1     
            total = 0 
            sufsum = 0 
            for i in range(d-1, -1, -1): 
                sufsum += arr[i]; 
                total += sufsum 
            return total 

        l, r = 1, 1e9 
        while l <= r: 
            mid = (r-l)//2+l 
            if numBoxes(mid) >= n: 
                r = mid-1 
            else: 
                l = mid+1 
        
        return int(l)

if __name__ == "__main__": 
    s = Solution() 

    assert s.minimumBoxes(3) == 3 