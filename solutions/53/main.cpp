/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov  6 13:43:12 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = INT32_MIN;
        int temp = 0;
        for (int i = 0; i < nums.size(); ++i) {
            temp += nums[i];
            if (temp > result)
                result = temp;
            if (temp <= 0)
                temp = 0;
        }
        return result;
    }
};

TEST(Test53, SimpleTest) {
    vector<int> nums{
        -2,1,-3,4,-1,2,1,-5,4
    };
    Solution s; 
    EXPECT_EQ(s.maxSubArray(nums), 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
