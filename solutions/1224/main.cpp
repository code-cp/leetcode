class Solution {
public:
    int maxEqualFreq(vector<int>& nums) {
        unordered_map<int, int> freq, count; 
        int res = 0, max_freq = 0; 
        for (int i = 0; i < nums.size(); ++i) {
            if (count[nums[i]] > 0) {
                freq[count[nums[i]]]--; 
            }
            count[nums[i]]++; 
            freq[count[nums[i]]]++; 

            max_freq = max(max_freq, count[nums[i]]); 

            bool ok = max_freq == 1 || 
                freq[max_freq] * max_freq + freq[max_freq-1] * (max_freq-1) == i+1 && freq[max_freq] == 1 || 
                freq[max_freq] * max_freq + 1 == i+1 && freq[1] == 1; 

            if (ok) {
                res = max(res, i+1); 
            }
        }
        return res; 
    }
};