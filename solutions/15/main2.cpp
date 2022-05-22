#include <unordered_set> 
#include <numeric>
#include <vector>
#include <gtest/gtest.h> 
#include <algorithm>

using namespace std; 

// use hash table 
// time complexity O(n^2) 
// space complexity O(n)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result; 
        sort(nums.begin(), nums.end());
        // to find a 
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) 
                return result; 
            // remove duplicated a 
            if (i > 0 && nums[i] == nums[i - 1]) 
                continue; 
            unordered_set<int> set; 
            // to find c
            for (int j = i + 1; j < nums.size(); ++j) {
                // remove duplicated c
                // not nums[j] == nums[j - 1] but nums[j] == nums[j - 1] && nums[j - 1] == nums[j - 2], see notes 
                if (j > i + 2 && nums[j] == nums[j - 1] && nums[j - 1] == nums[j - 2])
                    continue; 
                // to find b
                int b = 0 - (nums[i] + nums[j]);
                if (set.find(b) != set.end()) {
                    result.push_back({nums[i], b, nums[j]});
                    // remove duplicated b
                    set.erase(b); 
                }
                else 
                    set.insert(nums[j]); 
            }
        }
        return result; 
    }
};

TEST(Test15, SimpleTest)
{
    vector<int> nums = {-1,0,1,2,-1,-4};
    Solution s; 
    vector<vector<int>> results = s.threeSum(nums); 
    for (const auto& result : results)
    {
        EXPECT_EQ(accumulate(result.begin(), result.end(), 0), 0) << "Wrong answer"; 
    }
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}