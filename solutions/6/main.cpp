/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Nov 28 13:12:46 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    string convert(string s, int numRows) {
        // check input
        if (numRows == 1) return s;
        vector<string> result(numRows, "");
        int i = 0;
        int flag = -1;
        for (auto& c : s) {
            result[i] += c;
            if (i == 0 || i == numRows-1) flag = -flag;
            i += flag;
        }
        string res;
        for (auto& r : result) res += r;
        return res;
    }
};

TEST(Test6, SimpleTest) {
    string s = "PAYPALISHIRING"; 
    const int numRows = 3;
    string ans = "PAHNAPLSIIGYIR";
    Solution sol; 
    EXPECT_EQ(sol.convert(s, numRows), ans);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
