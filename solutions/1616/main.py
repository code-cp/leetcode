
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def checkForm(a, b):
            checkPal = lambda p: p == p[::-1]
            n = len(a)
            i, j = 0, n-1 
            while i < j:
                if a[i] != b[j]: 
                    break 
                i += 1 
                j -= 1 
            # make the palindrome check as small as possible 
            if checkPal(a[i:j+1]) or checkPal(b[i:j+1]):
                return True 
            return False 
        return checkForm(a, b) or checkForm(b, a) 
    
if __name__ == "__main__": 
    s = Solution() 

    a = "x" 
    b = "y" 
    assert s.checkPalindromeFormation(a, b)

    a = "abda" 
    b = "acmc"
    assert not s.checkPalindromeFormation(a, b)
      

    a = "abdef" 
    b = "fecab" 
    assert s.checkPalindromeFormation(a, b)
     

    a = "ulacfd" 
    b = "jizalu" 
    assert s.checkPalindromeFormation(a, b)
     
    
    a = "x"
    b = "y"
    assert s.checkPalindromeFormation(a, b)
            
        
                