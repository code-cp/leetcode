/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Nov  7 19:29:17 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int numFive = 0;
        int numTen = 0;
        for (auto& b : bills) {
            if (b == 5) numFive++;
            else if (b == 10) {
                numFive--;
                numTen++;
                if (numFive < 0) return false;
            }
            else {
                if (numTen > 0) {
                    numTen--;
                    numFive--;
                }
                else {
                    numFive -= 3;
                }
                if (numFive < 0 || numTen < 0) return false;
            }
        }
        return true;
    }
};

TEST(Test860, SimpleTest) {
    vector<int> bills{
        5,5,5,10,20
    };
    Solution s; 
    EXPECT_TRUE(s.lemonadeChange(bills));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
