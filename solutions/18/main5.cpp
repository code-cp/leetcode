#include <iostream>
#include <vector> 
#include <algorithm>
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

// use double pointer 
// but modified to deal with new test case 
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result; 
        sort(nums.begin(), nums.end());
        for (int k = 0; k < nums.size(); ++k) {
            if (k > 0 && nums[k] == nums[k-1])
                continue; 
            for (int i = k + 1; i < nums.size(); ++i) {
                if (i > k + 1 && nums[i] == nums[i - 1])
                    continue; 
                int left = i + 1; 
                int right = nums.size() - 1; 
                while (right > left) {
                    // to prevent overflow 
                    if (nums[k] + nums[i] > target - nums[left] - nums[right]) 
                        right--; 
                    // to prevent overflow 
                    else if (nums[k] + nums[i] < target - nums[left] - nums[right]) 
                        left++; 
                    else {
                        result.push_back({nums[k], nums[i], nums[left], nums[right]});
                        while (right > left && nums[right] == nums[right - 1]) 
                            right--; 
                        while (right < left && nums[left] == nums[left + 1])
                            left++; 
                        
                        right--; 
                        left++; 
                    }
                }
            }
        }
        return result; 
    }
};

TEST(Test18, SimpleTest)
{
    vector<int> nums = {1000000000, 1000000000, 1000000000, 1000000000};
    const int target = 0;
    Solution s; 
    vector<vector<int>> result = s.fourSum(nums, target);
    EXPECT_EQ(result.size(), 0); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
