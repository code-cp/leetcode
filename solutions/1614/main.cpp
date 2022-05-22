/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Jan  7 08:57:33 2022
> Description:   
 ************************************************************************/
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxDepth(string s) {
        int maxDepth = 0;
        int left = 0, right = 0;
        for (auto& c : s) {
            if (c == '(') left++;
            if (c == ')') {
                maxDepth = max(left - right, maxDepth);
                right++;
            }
        }
        return maxDepth;
    }
};

TEST(Test1614, SimpleTest) {
    string s = "(1+(2*3)+((8)/4))+1";
    Solution sol; 
    EXPECT_EQ(sol.maxDepth(s), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
