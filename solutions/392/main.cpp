/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 17:53:00 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool isSubsequence(string s, string t) {
        // dp table
        vector<vector<int>> dp(t.size()+1, vector<int>(s.size()+1, 0));
        // initialize
        for (int i = 0; i <= t.size(); ++i) {
            dp[i][0] = 1;
        }
        // traverse dp table
        for (int i = 1; i <= t.size(); ++i) {
            for (int j = 1; j <= s.size(); ++j) {
                if (t[i-1] == s[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[t.size()][s.size()] == 1;
    }
};

TEST(Test392, SimpleTest) {
    string s = "abc"; 
    string t = "ahbgdc"; 
    Solution sol; 
    EXPECT_TRUE(sol.isSubsequence(s, t));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
