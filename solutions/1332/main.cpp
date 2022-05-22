/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Jan 22 09:01:30 2022
> Description:   
 ************************************************************************/
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int removePalindromeSub(string s) {
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != s[s.size()-i-1]) return 2;
        }
        return 1;
    }
};

TEST(Test1332, SimpleTest) {
    string s = "baabb"; 
    Solution sol; 
    EXPECT_EQ(sol.removePalindromeSub(s), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}