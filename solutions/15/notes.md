## remove duplicates 

- when using `unodered_set`, need to remove duplicates using 
```
if (j > i + 2 && nums[j] == nums[j - 1] && nums[j - 1] == nums[j - 2])
    continue; 
```
1. we cannot use `nums[j] == nums[j - 1]` only since it will remove a valid solution of `2, -1, -1`
2. we cannot omit this condition, see example below 

```
input: [0,2,2,3,0,1,2,3,-1,-4,2]
output: [[-4,2,2],[-4,2,2],[-4,1,3],[-1,0,1]]
correct answer: [[-4,1,3],[-4,2,2],[-1,0,1]]
```

The input after sorting is `-4, -1, 0, 0, 1, 2, 2, 2, 2, 3, 3`, when `i=0`, `j=7`, the `2, 2, 2` satisfies the conditions of `j > i + 2 && nums[j] == nums[j - 1] && nums[j - 1] == nums[j - 2]`, so `2` will be skipped. 

