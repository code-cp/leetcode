/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 15 10:49:33 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int result = 0;
        for (int i = 1; i <= nums.size(); ++i) {
            result ^= i ^ nums[i-1];
        }
        return result;
    }
};

TEST(Test268, SimpleTest) {
    vector<int> nums{
        3,0,1
    };
    Solution s; 
    EXPECT_EQ(s.missingNumber(nums), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
