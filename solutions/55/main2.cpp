#include <iostream>
#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    bool canJump(vector<int>& nums) {
        // the rightmost index can reach 
        int farthest = 0; 

        for (int i = 0; i <= farthest && farthest < nums.size() - 1; ++i)
        {
            farthest = max(farthest, i + nums[i]);
        }

        return farthest >= nums.size() - 1; 
    }
};

TEST(Test55, SimpleTest)
{
    vector<int> nums = {2,3,1,1,4};
    Solution s; 
    EXPECT_TRUE(s.canJump(nums));
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
