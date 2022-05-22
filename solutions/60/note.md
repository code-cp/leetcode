- easy solution is to call `nextPermutation` function in leetcode 31, but it takes `O(kn)` time 
- the hardest step is to start with `k-1` instead of `k`, can think it this way 
1. if input is 1, then just return original sequence 
2. if input is 2, then deal with k = 1 first, just need to find the next number of original sequence 
- the index of array starts with 0, so need to start with `k-1` 
