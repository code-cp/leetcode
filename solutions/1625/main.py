class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        res = s 
        # add in odd and even 
        for i in range(10): 
            for j in range(10): 
                t = list(s) 
                if b%2 == 1: 
                    for k in range(0, n, 2): 
                        t[k] = (int(t[k])+i*a)%10 
                        t[k] = str(t[k])
                for k in range(1, n, 2): 
                    t[k] = (int(t[k])+j*a)%10 
                    t[k] = str(t[k])
                # rotate 
                p = [x for x in t]
                for k in range(n): 
                    p = p[n-b:]+p[:n-b]
                    res = min(res, "".join(p))
        return res 
                    
                         