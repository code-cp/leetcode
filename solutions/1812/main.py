class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        convert = lambda c: (ord(c[0])-ord("a"), ord(c[1])-ord("1"))
        co = convert(coordinates)
        if (co[0]+co[1]) % 2 == 0: 
            return False 
        else: 
            return True 