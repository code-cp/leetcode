# //              0
# //          /        \   
# //      0                1
# //    /   \            /    \
# //  0       1        1       0
# // / \     /  \     /  \    / \ 
# //0   1   1    0   1    0  0   1

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: 
            return 0 
        par = self.kthGrammar(n-1, (k+1)//2)
        # NOTE, k is 1-indexed 
        if par == 0:
            return 1 if k % 2 == 0 else 0 
        else: 
            return 0 if k % 2 == 0 else 1 



