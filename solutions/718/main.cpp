/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 14:52:09 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int result = 0;
        // dp table
        // dp[i][j] means the max len for nums1[0:i-1], and nums2[0:j-1]
        vector<vector<int>> dp(nums1.size()+1, vector<int>(nums2.size()+1, 0));
        // initialize
        // pass
        // traverse dp table
        for (int i = 1; i <= nums1.size(); ++i) {
            for (int j = 1; j <= nums2.size(); ++j) {
                if (nums1[i-1] == nums2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if (result < dp[i][j]) result = dp[i][j];
                }
            }
        }
        return result;
    }
};

TEST(Test718, SimpleTest) {
    vector<int> nums1{
        1,2,3,2,1
    };
    vector<int> nums2{
        3,2,1,4,7
    };
    Solution s; 
    int result = s.findLength(nums1, nums2); 
    EXPECT_EQ(result, 3);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
