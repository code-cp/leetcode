/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 12:50:16 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        // dp table
        vector<vector<int>> dp(s.size(), vector<int>(s.size(), 0));
        // initialize
        for (int i = 0; i < s.size(); ++i)
            dp[i][i] = 1;
        // traverse dp table
        for (int i = s.size()-1; i >= 0; --i) {
            for (int j = i+1; j < s.size(); ++j) {
                if (s[i] == s[j]) dp[i][j] = dp[i+1][j-1]+2;
                else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][s.size()-1];
    }
};

TEST(Test516, SimpleTest) {
    string s = "bbbab"; 
    Solution sol; 
    EXPECT_EQ(sol.longestPalindromeSubseq(s), 4); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
