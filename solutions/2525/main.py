class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        dim_thresh = 10**4 
        vol_thresh = 10**9 
        mass_thresh = 100
        
        bulky = False 
        if length >= dim_thresh or width >= dim_thresh or height >= dim_thresh:
            bulky = True
        if height * width * length >= vol_thresh: 
            bulky = True 
        
        heavy = False 
        if mass >= mass_thresh: 
            heavy = True
            
        if bulky and heavy: 
            return "Both"
        elif not bulky and not heavy: 
            return "Neither"
        elif bulky and not heavy: 
            return "Bulky"
        else: 
            return "Heavy" 
         