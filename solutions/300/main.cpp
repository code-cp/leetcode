/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 10:51:33 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // dp table
        // initialize
        vector<int> dp(nums.size(), 1);
        // traverse dp table
        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] > nums[j])
                    dp[i] = max(dp[i], dp[j] + 1);
            }
        }
        return *max_element(dp.begin(), dp.end());
    }
};

TEST(Test300, SimpleTest) {
    vector<int> nums{
        10,9,2,5,3,7,101,18
    };
    Solution s; 
    EXPECT_EQ(s.lengthOfLIS(nums), 4); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
