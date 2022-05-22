#include <iostream> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        // check input 
        if (nums.empty())
            return true; 

	// 是男人就下一百层解法
        int leftmost = nums.size() - 1; 

        for (int i = nums.size() - 2; i >= 0; --i)
        {
            if (i + nums[i] >= leftmost)
                leftmost = i; 
        }

        return leftmost == 0; 
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
