from typing import * 

# ref 1017
# N=a3(-2)^3+ a2(-2)^2+ a1(-2)^1+ a0(-2)^0
# N=（-a3)*2^3+(a2)*2^2+(-a1)*2^1+(a0)*2^0
# by N&1 we take out the last coefficient a0 everytime, by >>1 we cross out a0, then N=-N will make the (-a1) to (a1)
# N= (-a3)*2^3+(a2)*2^2+(-a1)*2^1+(a0)*2^0 we get a0
# -N= (a3)*2^2+ (-a2)*2^1+(a1)*2^0 we get a1
# N= (-a3)*2^1+ (a2)*2^0 we get a2
# -N= (a3)*2^0 we get a3

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def toBase10(num): 
            n = len(num)
            ans = 0
            for i in range(n):  
                ans += (-2)**i * num[n-1-i]
            return ans 
        
        a1 = toBase10(arr1)
        a2 = toBase10(arr2)
        a = a1+a2
        
        if a == 0: 
            return [0]
    
        ans = [] 
        while a != 0 and a != 1: 
            ans.append(a&1)
            a >>= 1 
            a *= -1 
        if a != 0: 
            ans.append(a)
        
        return ans[::-1] 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.addNegabinary([1,1,1,1,1], [1,0,1]) == [1,0,0,0,0]
    # assert s.addNegabinary([0], [1,0]) == [1,0]
    # assert s.addNegabinary([0], [1,1]) == [1,1]
        
            