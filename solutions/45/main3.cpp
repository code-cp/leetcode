#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int jump(vector<int>& nums) {
        
        // check input 
        if (nums.size() < 2)
            return 0; 
        
        int step = 0; 
        int left = 0; 
        int right = 0; 
        int prev_right, cur_right; 

        while (left <= right)
        {
            ++step;
            prev_right = right; 
            for (int i = left; i <= prev_right; ++i)
            {
                cur_right = i + nums[i]; 
                if (cur_right >= nums.size() - 1) 
                    return step; 
                if (cur_right > right)
                    right = cur_right; 
            }
            left = prev_right + 1; 
        }
        return step; 
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
