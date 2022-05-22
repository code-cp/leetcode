/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 09:48:13 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
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
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                }
                else {
                    dp[i][j] = min({dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2});
                }
            }
        }
        return dp[word1.size()][word2.size()];
    }
};

TEST(Test583, SimpleTest) {
    string word1 = "leetcode";
    string word2 = "etco";
    Solution s; 
    EXPECT_EQ(s.minDistance(word1, word2), 4);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
