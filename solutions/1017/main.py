
# https://leetcode.com/problems/convert-to-base-2/solutions/265507/java-c-python-2-lines-exactly-same-as-base-2/

# N=a3(-2)^3+ a2(-2)^2+ a1(-2)^1+ a0(-2)^0
# N=（-a3)*2^3+(a2)*2^2+(-a1)*2^1+(a0)*2^0
# by N&1 we take out the last coefficient a0 everytime, by >>1 we cross out a0, then N=-N will make the (-a1) to (a1)
# N= (-a3)*2^3+(a2)*2^2+(-a1)*2^1+(a0)*2^0 we get a0
# -N= (a3)*2^2+ (-a2)*2^1+(a1)*2^0 we get a1
# N= (-a3)*2^1+ (a2)*2^0 we get a2
# -N= (a3)*2^0 we get a3

class Solution:
    def baseNeg2(self, n: int) -> str:
        
        # def base2(n):
        #     if n == 0 or n == 1: 
        #         return str(n)
        #     return base2(n>>1)+str(n&1)
        
        if n == 0 or n == 1: 
            return str(n)
        return self.baseNeg2(-(n>>1))+str(n&1)