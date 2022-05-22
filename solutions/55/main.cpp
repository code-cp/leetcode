#include <iostream>
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool canJump(vector<int>& nums) {

        // initialize dp table 
        vector<int> dp(nums.size(), 0);

        for (int i = 1; i < nums.size(); ++i)
        {
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1; 
            if (dp[i] < 0)
                return false; 
        }

        return true; 
    }
};

TEST(Test55, SimpleTest)
{
    vector<int> nums = {2,3,1,1,4}; 
    Solution s; 
    EXPECT_TRUE(s.canJump(nums)) << "Wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
