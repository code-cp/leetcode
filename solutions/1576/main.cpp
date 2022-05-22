/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Jan  5 11:05:21 2022
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
    char replaceChar(const vector<char>& chars) {
        string allChars = "abcdefghijklmnopqrstuvwxyz";
        for (const auto& c : allChars) {
            if (find(chars.begin(), chars.end(), c) != chars.end())
            continue;
            return c;
        }
        return 'a';
    }
    string modifyString(string s) {
        s = "?" + s + "?";
        vector<char> chars;
        for (int i = 1; i < s.size()-1; ++i) {
            if (s[i] == '?') {
                if (s[i-1] != '?') chars.push_back(s[i-1]);
                if (s[i+1] != '?') chars.push_back(s[i+1]);
                s[i] = replaceChar(chars);
                chars.clear();
            }
        }
        return s.substr(1, s.size()-2);
    }
};

TEST(Test1576, SimpleTest) {
    string s = "?zs"; 
    Solution sol; 
    string result = sol.modifyString(s);
    string answer = "azs";
    EXPECT_TRUE(equal(result.begin(), result.end(), answer.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
