- `bind_front`, discussed in [this video](https://youtu.be/7pqPfQ_HpmI), but not supported with g++ 12.0.0 
- need to use `find_if` instead
```
Returns an iterator to the first element in the range [first,last) for which pred returns true. If no such element is found, the function returns last
```
- `reverse_iterator` 
```
when provided with a bidirectional iterator, std::reverse_iterator produces a new iterator that moves from the end to the beginning of the sequence defined by the underlying bidirectional iterator
```
- time complexity is `O(n)`, space complexity `O(1)` 
