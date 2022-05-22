/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Dec 20 15:50:20 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    long long countVowels(string word) {
        vector<char> vowels{'a', 'e', 'i', 'o', 'u'};
        auto checkVowel = [&](char x) {
            return find(vowels.begin(), vowels.end(), x) != vowels.end();
        };
        // dp table
        vector<long long> dp(word.size(), 0);
        // initialize
        dp[0] = checkVowel(word[0]) ? 1 : 0;
        // traverse dp table
        for (int i = 1; i < word.size(); ++i) {
            if (checkVowel(word[i])) dp[i] = dp[i-1] + i + 1;
            else dp[i] = dp[i-1];
        }
        long long result = 0;
        result = accumulate(dp.begin(), dp.end(), result);
        return result;
    }
};

TEST(Test2063, SimpleTest) {
    string word = "noosabasboosa";
    Solution s; 
    EXPECT_EQ(s.countVowels(word), 237);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
