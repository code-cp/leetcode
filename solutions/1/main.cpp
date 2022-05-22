#include <iostream>
#include <vector>
#include <unordered_map> 
#include <gtest/gtest.h>

using namespace std; 

// time complexity O(n)
// space complexity O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> table; 
        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            auto itr = table.find(diff); 
            if (itr != table.end()) {
                return {itr->second, i}; 
            }
            else {
                // note key is number, not index 
                table.insert(pair<int, int>(nums[i], i));
            }
        }
        return {}; 
    }
};

TEST(Test1, SimpleTest)
{
    vector<int> nums = {2,7,11,15}; 
    int target = 9; 
    Solution s; 
    vector<int> result = s.twoSum(nums, target);
    EXPECT_EQ(result[0], 0);
    EXPECT_EQ(result[1], 1); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
} 
