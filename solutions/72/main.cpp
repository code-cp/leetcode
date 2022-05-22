/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 10:45:11 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int minDistance(string word1, string word2) {
        // dp table
        vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1, 0));
        // initialize
        dp[0][0] = 0;
        for (int i = 1; i <= word1.size(); ++i)
            dp[i][0] = i;
        for (int j = 1; j <= word2.size(); ++j)
            dp[0][j] = j;
        // traverse dp table
        for (int i = 1; i <= word1.size(); ++i) {
            for (int j = 1; j <= word2.size(); ++j) {
                if (word1[i-1] == word2[j-1]) dp[i][j] = dp[i-1][j-1];
                else {
                    // delete word1, delete word2, or replace
                    dp[i][j] = min({dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1});
                }
            }
        }
        return dp[word1.size()][word2.size()];
    }
};

TEST(Test72, SimpleTest) {
    string word1 = "horse";
    string word2 = "ros"; 
    Solution s; 
    EXPECT_EQ(s.minDistance(word1, word2), 3);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
