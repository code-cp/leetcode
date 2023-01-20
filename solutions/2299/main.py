class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: 
            return False 
        ol = False 
        ou = False 
        od = False 
        osc = False 
        no_adj = True 
        pre = None 
        for p in password: 
            if p.islower():
                ol = True 
            if p.isupper():
                ou = True 
            if p.isdigit():
                od = True 
            if p in "!@#$%^&*()-+":
                osc = True 
            if pre: 
                if p == pre: 
                    no_adj = False 
            pre = p 
        return ol and ou and od and osc and no_adj