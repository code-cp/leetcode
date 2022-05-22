/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 10 13:48:06 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        vector<int> dp(2, 0);
        dp[0] = 0;
        dp[1] = 1;
        int sum;
        for (int i = 2; i <= n; ++i) {
            sum = dp[1] + dp[0];
            swap(dp[0], dp[1]);
            dp[1] = sum;
        }
        return sum;
    }
};

TEST(Test509, SimpleTest) {
    const int n = 4; 
    Solution s; 
    EXPECT_EQ(s.fib(n), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
