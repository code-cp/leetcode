/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov 16 14:28:11 2021
> Description:   
 ************************************************************************/
#include <stack> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        stack<int> st;
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            if (n & 1)
                st.push(1);
            else
                st.push(0);
            n = n >> 1;
        }
        for (int i = 0; i < 32; i++) {
            result |= (st.top() << i);
            st.pop();
        }
        return result;
    }
};

TEST(Test190, SimpleTest) {
    const int n = 43261596;
    Solution s; 
    EXPECT_EQ(s.reverseBits(n), 964176192);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
