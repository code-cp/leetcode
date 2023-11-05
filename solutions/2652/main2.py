class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(map(
            # k(k+1)/2*m
            lambda x: x[0]*(n//x[0]+1)*(n//x[0])//2 * x[1],
            [(3,1), (5,1), (7,1), (15,-1), (21, -1), (35, -1), (105, 1)]
        ))