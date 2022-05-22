/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 15 09:58:09 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x ^ y;
        int count = 0;
        while (z != 0) {
            if ((z & 1) == 1)
                count++;
            z = z >> 1;
        }
        return count;
    }
};

TEST(Test461, SimpleTest) {
    const int x = 1; 
    const int y = 4;
    Solution s; 
    EXPECT_EQ(s.hammingDistance(x, y), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
