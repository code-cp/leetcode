class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        pre = None 
        for t in tokens: 
            if t[0].isdigit():
                if pre is None: 
                    pre = int(t)
                elif int(t) <= pre:
                    return False
                else: 
                    pre = int(t)
        return True  
