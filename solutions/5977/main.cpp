/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan  9 17:03:31 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int minSwaps(vector<int>& nums) {
        const int n = nums.size();
        const int winSize = accumulate(nums.begin(), nums.end(), 0);
        if (winSize == 0) return 0;
        nums.insert(nums.end(), nums.begin(), nums.end());
        int curSwap = 0, minSwap = INT_MAX;
        for (int i = 0; i < n+winSize; ++i) {
            curSwap += (1-nums[i]);
            if (i >= winSize-1) {
                minSwap = min(curSwap, minSwap);
                curSwap -= (1-nums[i+1-winSize]);
            }
        }
        return minSwap;
    }
};

TEST(Test5977, SimpleTest) {
    vector<int> nums{
        0,1,0,1,1,0,0
    };
    Solution s; 
    EXPECT_EQ(s.minSwaps(nums), 1);
}
