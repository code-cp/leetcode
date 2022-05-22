class Solution:
    def __init__(self): 
        self.fibs = []
    def generateFibs(self, n): 
        if n <= len(self.fibs): 
            return self.fibs[n-1]
        if n == 1: 
            self.fibs.append(1) 
            return 1 
        if n == 2: 
            self.fibs.append(1) 
            return 1 
        fib = self.generateFibs(n-1) + self.generateFibs(n-2)
        self.fibs.append(fib)
        return fib 
    def findMinFibonacciNumbers(self, k: int) -> int:
        n = 1 
        while self.generateFibs(n) < k: 
            n += 1 
        n -= 1 
        result = 0 
        while k > 0: 
            while k < self.fibs[n]:
                n -= 1 
            k -= self.fibs[n]
            result += 1 
        return result 

if __name__ == "__main__": 
    k = 7
    s = Solution()
    assert s.findMinFibonacciNumbers(k) == 2 