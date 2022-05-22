/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov 26 20:34:36 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int numDistinct(string s, string t) {
        // dp table
        vector<vector<int>> dp(s.size()+1, vector<int>(t.size()+1, 0));
        // initialize
        dp[0][0] = 1;
        for (int i = 1; i <= t.size(); ++i)
            dp[0][i] = 0;
        for (int j = 1; j <= s.size(); ++j)
            dp[j][0] = 1;
        // traverse dp table
        for (int i = 1; i <= s.size(); ++i) {
            for (int j = 1; j <= t.size(); ++j) {
                if (s[i-1] == t[j-1]) {
                    // to prevent overflow
                    if (dp[i-1][j-1] < INT_MAX - dp[i-1][j])
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                }
                else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[s.size()][t.size()];
    }
};

TEST(Test115, SimpleTest) {
    string s = "rabbbit";
    string t = "rabbit";
    Solution sol; 
    EXPECT_EQ(sol.numDistinct(s, t), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
