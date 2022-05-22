/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan  2 15:03:52 2022
> Description:   
 ************************************************************************/
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int lastRemaining(int n) {
        int remain = n, step = 1, head = 1;
        bool fromLeft = true;
        while (remain > 1) {
            if (fromLeft || remain % 2 == 1) {
                head += step;
            }
            step *= 2;
            remain /= 2;
            fromLeft = !fromLeft;
        }
        return head;
    }
};

TEST(Test390, SimpleTest) {
    Solution s; 
    const int n = 9; 
    EXPECT_EQ(s.lastRemaining(n), 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
