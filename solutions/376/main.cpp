/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov  6 10:59:29 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        int curDiff = 0;
        int preDiff = 0;
        int result = 1;
        for (int i = 0; i < nums.size()-1; ++i) {
            curDiff = nums[i+1] - nums[i];
            if ((curDiff > 0 && preDiff <= 0) || (preDiff >= 0 && curDiff < 0)) {
                result++;
                preDiff = curDiff;
            }
        }
        return result;
    }
};

TEST(Test376, SimpleTest) {
    vector<int> nums{
        1,7,4,9,2,5
    };
    Solution s;
    EXPECT_EQ(s.wiggleMaxLength(nums), 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
