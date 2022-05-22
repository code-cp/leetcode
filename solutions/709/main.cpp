/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Dec 11 15:37:27 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    string toLowerCase(string s) {
        for (auto& c : s) {
            if (c >= 'A' && c <= 'Z') c |= 32;
        }
        return s;
    }
};

TEST(Test709, SimpleTest) {
    string s = "Hello";
    Solution sol; 
    string ans = "hello";
    EXPECT_EQ(sol.toLowerCase(s), ans);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
