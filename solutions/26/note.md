## distance 

- another solution is use `distance` 
```
class Solution { 
public: 
    int RemoveDuplicates(vector<int>& nums) {
        return distance(nums.begin(), unique(nums.begin(), nums.end()));
    }
};
```
- time complexity is O(n), space complexity is O(1)
- distance calculates the number between iterators 
- unique removes consecutive duplicates, returns the iterator of the last element not removed 

## upper_bound 

```
class Solution {
public: 
    int RemoveDuplicates(vector<int>& nums) { 
        return distance(nums.begin(), RemoveDuplicates(nums.begin(), numes.end(), nums.begin())); 
    }

    template<typename InIt, typename OutIt>
    RemoveDuplicates(InIt first, InIt last, OutIt output) { 
        while (first != last) {
            *output = *first; 
	    output++; 
	    first = upper_bound(first, last, *first); 
	}
        return output; 
    }
}; 
```
- `upper_bound` returns the iterator pointing to the first element in range `[first, last)` which compares greater than input value 
	
