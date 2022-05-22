/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov 16 14:03:59 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        // dp table, initialize to 0
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        // iterate items
        for (const auto& str : strs) {
            // calculate the weights
            int zeroNum = 0, oneNum = 0;
            for (const auto& s : str) {
                if (s == '0') zeroNum++;
                else oneNum++;
            }
            // iterate bag size
            for (int i = m; i >= zeroNum; i--) {
                for (int j = n; j >= oneNum; j--)
                    dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum] + 1);
            }
        }
        return dp[m][n];
    }
};

TEST(Test474, SimpleTest) {
    vector<string> strs{
        "10","0001","111001","1","0"
    };
    const int m = 5; 
    const int n = 3;
    Solution s; 
    EXPECT_EQ(s.findMaxForm(strs, m, n), 4);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
