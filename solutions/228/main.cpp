class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans; 
        auto f = [&](int start, int end) {
            return start == end ? to_string(nums[start]) : to_string(nums[start]) + "->" + to_string(nums[end]); 
        }; 

        for (int start = 0, end, n = nums.size(); start < n; start = end + 1) {
            end = start; 
            while (end + 1 < n && nums[end + 1] == nums[end] + 1) end++; 
            ans.emplace_back(f(start, end));  
        }

        return ans; 
    }
};