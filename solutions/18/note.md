## brute force 

- time complexity O(n^3)
- for unique 
```
The removal is done by replacing the duplicate elements by the next element that is not a duplicate, and signaling the new size of the shortened range by returning an iterator to the element that should be considered its new past-the-end element
```
- for erase 
```
Removes from the vector either a single element (position) or a range of elements ([first,last))
```

## use hashtable 

- store the sum of two numbers first, then find the two numbers left 
- to avoid duplicate, need to make sure `i < j < k < m`
- time complexity is O(n^4), space complexity is O(n^2) 

## use hashmap 

- find the sum of every two pairs of numbers 
- find x + y = target, where x, y are sums of one pair 
- time complexity `O(n^2)`, space complexity `O(n^2)` 
- `equal_range` 
```
Returns the bounds of a range that includes all the elements in the container which have a key equivalent to k.
```
