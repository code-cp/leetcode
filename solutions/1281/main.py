class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total, prod = 0, 1 
        while n > 0: 
            total += n % 10 
            prod *= n % 10 
            n //= 10 
        return prod - total 
     
        