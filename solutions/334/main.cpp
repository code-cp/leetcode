/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Jan 12 09:55:26 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int firstVal = INT_MAX, secondVal = INT_MAX;
        int firstId = 0, secondId = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] < firstVal) {
                firstVal = nums[i];
                firstId = i;
            }
            else if (nums[i] > firstVal && nums[i] < secondVal) {
                secondVal = nums[i];
                secondId = i;
            }
            else if (nums[i] > secondVal) return true;
        }
        return false;
    }
};

TEST(Test334, SimpleTest) {
    vector<int> nums{
        20,100,10,12,5,13
    };
    Solution s; 
    EXPECT_TRUE(s.increasingTriplet(nums));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
