- time complexity `O(n)`, space complexity `O(1)` 
- can also use `remove` in C++
```
class Solution 
{
public: 
    int removeElement(vector<int>& nums, int target) {
	return distance(nums.begin(), remove(nums.begin(), nums.end(), target)); 
    }
};
```
