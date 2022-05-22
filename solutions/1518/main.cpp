/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Dec 16 10:04:56 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    void drink(int full, int empty, int numExchange, int& result) {
        result += full;
        // base case
        if (full + empty < numExchange) {
            return;
        }
        // recursion
        empty += full;
        full = 0;
        full = int(empty / numExchange);
        empty = empty % numExchange;
        drink(full, empty, numExchange, result);
    }
    int numWaterBottles(int numBottles, int numExchange) {
        int result = 0;
        drink(numBottles, 0, numExchange, result);
        return result;
    }
};

TEST(Test1518, SimpleTest) {
    const int numBottles = 9; 
    const int numExchange = 3; 
    Solution s; 
    EXPECT_EQ(s.numWaterBottles(numBottles, numExchange), 13);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
