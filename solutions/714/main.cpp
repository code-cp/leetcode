/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 10 09:23:52 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int result = 0;
        int minPrice = INT32_MAX;
        for (auto& p : prices) {
            if (minPrice > p) {
                minPrice = p;
            }
            else {
                if (p - minPrice > fee) {
                    result += p - minPrice - fee;
                    minPrice = p - fee;
                }
            }
        }
        return result;
    }
};

TEST(Test714, SimpleTest) {
    vector<int> prices{
        1,3,2,8,4,9
    };
    const int fee = 2;
    Solution s; 
    EXPECT_EQ(s.maxProfit(prices, fee), 8);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
