/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 16:53:30 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        // dp table
        vector<vector<int>> dp(nums1.size()+1, vector<int>(nums2.size()+1, 0));
        // initialize
        // pass
        // traverse dp table
        for (int i = 1; i <= nums1.size(); ++i) {
            for (int j = 1; j <= nums2.size(); ++j) {
                if (nums1[i-1] == nums2[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;
                else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[nums1.size()][nums2.size()];
    }
};

TEST(Test1035, SimpleTest) {
    vector<int> nums1{
        1,4,2
    };
    vector<int> nums2{
        1,2,4
    };
    Solution s; 
    EXPECT_EQ(s.maxUncrossedLines(nums1, nums2), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
