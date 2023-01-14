class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        original = perm.copy()
        for j in range(n):  
            arr = [0] * n 
            for i in range(n): 
                if i % 2 == 0: 
                    arr[i] = perm[i // 2]
                else: 
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            if arr == original: 
                return j+1
            else: 
                perm = arr 

if __name__ == "__main__": 
    s = Solution() 

    assert s.reinitializePermutation(4) == 2 