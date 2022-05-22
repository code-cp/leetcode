/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Nov  7 11:23:50 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <numeric>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    static bool cmp(int a, int b) {
        return abs(a) > abs(b);
    }
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end(), cmp);
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < 0 && k > 0) {
                nums[i] *= -1;
                k--;
            }
        }
        if (k % 2 == 1)
            nums[nums.size()-1] *= -1;
        int result = 0;
        result = accumulate(nums.begin(), nums.end(), result);
        return result;
    }
};

TEST(Test1005, SimpleTest) {
    vector<int> nums{
        4,2,3
    };
    const int k = 1;
    Solution s; 
    EXPECT_EQ(s.largestSumAfterKNegations(nums, k), 5);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
