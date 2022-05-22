class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # base case 
        if sx == tx and sy == ty:
            return True
        if tx < sx or ty < sy:
            return False 
        
        if tx == sx and ty != sy: 
            if ty > sy:
                if (ty - sy) % tx == 0:
                    return True
        
        if ty == sy and tx != sx: 
            if tx > sx: 
                if (tx - sx) % ty == 0:
                    return True 

        if tx > ty: 
            return self.reachingPoints(sx, sy, tx % ty, ty)
        else: 
            return self.reachingPoints(sx, sy, tx, ty % tx)

if __name__ == "__main__": 
    s = Solution() 

    sx = 1
    sy = 1
    tx = 3
    ty = 5
    assert s.reachingPoints(sx, sy, tx, ty) 