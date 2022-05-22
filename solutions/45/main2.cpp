#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int jump(vector<int>& nums) {
        // maximum index already reached  
        int prev_max = 0;
        // maximum index could reach by using result + 1 steps  
        int cur_max = 0; 
        // minimum number of steps for largest i 
        int result = 0; 

        for (int i = 0; i < nums.size(); i++)
        {
            if (i > prev_max)
            {
                prev_max = cur_max; 
                // we must make one more jump to reach here 
                ++result;
            }
            cur_max = max(cur_max, i + nums[i]); 
        }

        return result; 
    }
};

TEST(Test45, SimpleTest)
{
    vector<int> nums = {1,2,3};
    Solution s; 
    EXPECT_EQ(s.jump(nums), 2) << "wrong answer";
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
