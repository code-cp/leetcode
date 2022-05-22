/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Jan 13 08:45:16 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        long long max_val = INT_MIN, max_id = 0, second_mval = INT_MIN;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > max_val) {
                second_mval = max_val;
                max_val = nums[i];
                max_id = i;
            }
            else if (nums[i] > second_mval) second_mval = nums[i];
        }
        if (max_val >= 2*second_mval) return max_id;
        else return -1;
    }
};

TEST(Test747, SimpleTest) {
    vector<int> nums{
        3,6,1,0
    };
    Solution s; 
    EXPECT_EQ(s.dominantIndex(nums), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
