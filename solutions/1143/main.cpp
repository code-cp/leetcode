/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 15:35:07 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // dp table
        vector<vector<int>> dp(text1.size()+1, vector<int>(text2.size()+1, 0));
        // initialize
        // pass
        // traverse dp table
        for (int i = 1; i <= text1.size(); ++i) {
            for (int j = 1; j <= text2.size(); ++j) {
                if (text1[i-1] == text2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
                else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[text1.size()][text2.size()];
    }
};

TEST(Test1143, SimpleTest) {
    string text1 = "abcde";
    string text2 = "ace";
    Solution s; 
    EXPECT_EQ(s.longestCommonSubsequence(text1, text2), 3);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
