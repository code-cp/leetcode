/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 11:43:35 2021
> Description:   
 ************************************************************************/
#include <numeric> 
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int countSubstrings(string s) {
        // dp table
        vector<vector<int>> dp(s.size(), vector<int>(s.size(), 0));
        // initialize
        for (int i = 0; i < s.size(); ++i) dp[i][i] = 1;
        // traverse dp table
        for (int i = s.size()-1; i >= 0; --i) {
            for (int j = i+1; j < s.size(); ++j) {
                if (s[i] == s[j]) {
                    if (i == j-1) dp[i][j] = 1;
                    else dp[i][j] = dp[i+1][j-1];
                }
            }
        }
        // get result
        int sum = 0;
        for (auto& row : dp) {
            sum = accumulate(row.begin(), row.end(), sum);
        }
        return sum;
    }
};

TEST(Test647, SimpleTest) {
    string s = "aaa"; 
    Solution sol; 
    EXPECT_EQ(sol.countSubstrings(s), 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
