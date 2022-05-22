/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Dec  4 15:34:39 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    int m;
    int quickPowMod(int a, int b) {
        a %= m;
        if (a == 0) return 0;
        int result = 1;
        while (b > 0) {
            if (b & 1) result = (result * a) % m;
            b >>= 1;
            a = (a*a) % m;
        }
        return result;
    }
public:
    Solution() : m(1337) {}
    int superPow(int a, vector<int>& b) {
        int result = 1;
        reverse(b.begin(), b.end());
        for (auto& n : b) {
            result = (result * quickPowMod(a, n)) % m;
            a = quickPowMod(a, 10);
        }
        return result;
    }
};

TEST(Test372, SimpleTest) {
    const int a = 2147483647;
    vector<int> b{
        2, 0, 0
    };
    Solution s; 
    EXPECT_EQ(s.superPow(a, b), 1198);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
