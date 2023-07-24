class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0 
        ans += min(numOnes, k)
        if k > numOnes+numZeros:
            ans -= min(k-numOnes-numZeros, numNegOnes)
        return ans 
            