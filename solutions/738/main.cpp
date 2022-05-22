/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 10 08:49:30 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string strNum = to_string(n);
        int flag = strNum.size();
        for (int i = strNum.size()-1; i > 0; i--) {
            if (strNum[i-1] > strNum[i]) {
                flag = i;
                strNum[i-1]--;
            }
        }
        for (int i = flag; i < strNum.size(); i++) {
            strNum[i] = '9';
        }
        return stoi(strNum);
    }
};

TEST(Test738, SimpleTest) {
    const int n = 10; 
    Solution s; 
    EXPECT_EQ(s.monotoneIncreasingDigits(n), 9);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
