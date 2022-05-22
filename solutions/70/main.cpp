#include <iostream>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int climbStairs(int n) {
        int f_n_1 = 1, f_n_2 = 1, temp; 

        if (n == 1)
            return 1; 

        for (int i = 1; i < n; ++i)
        {
            temp = f_n_1;
            f_n_1 += f_n_2;
            f_n_2 = temp;  
        }
        return f_n_1; 
    }
};

TEST(Test70, SimpleTest)
{
    const int n = 3; 
    Solution s; 
    EXPECT_EQ(s.climbStairs(n), 3) << "wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
