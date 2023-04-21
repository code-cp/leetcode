class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # return n if n%2 == 0 else n*2
        # 最小公倍数 = （num1 * num2）/ 最大公约数
        def gcd(a, b): 
            if b == 0: 
                return a 
            return gcd(b, a%b)
        return int(2*n/gcd(2, n)) 