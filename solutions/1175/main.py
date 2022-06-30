import math 
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def checkPrime(n): 
            if n <= 1: 
                return False 
            for i in range(2, math.floor(math.sqrt(n))+1):
                if n % i == 0:
                    return False 
            return True 

        prime_cnt = 0 
        for i in range(1, n+1): 
            if checkPrime(i):
                prime_cnt += 1 

        res = math.factorial(prime_cnt) % (10**9 + 7)
        res *= math.factorial(n - prime_cnt) % (10**9 + 7)
        return res % (10**9 + 7)

if __name__ == "__main__": 
    s = Solution()

    assert s.numPrimeArrangements(5) == 12 
    assert s.numPrimeArrangements(100) == 682289015 