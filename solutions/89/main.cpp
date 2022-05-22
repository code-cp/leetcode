#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity ? 
    // space complexity O(2^n)
    vector<int> grayCode(int n) {
        vector<int> dp;
        dp.reserve(1<<n);

        int count = 0, to_add = 0, value = 0; 

        dp.push_back(0);

        for (int i = 1; i <= n; ++i)
        {
            count = 1 << i; 
            to_add = 1 << (i - 1);   

            for (int j = count / 2; j < count; ++j)
            {
                value = dp[count - 1 - j] + to_add; 
                dp.push_back(value); 
            }
        }

        return dp; 
    }
};

TEST(Test89, SimpleTest)
{
    const int n = 2; 
    Solution s; 
    vector<int> result = s.grayCode(n);
    EXPECT_EQ(result[0], 0); 
    EXPECT_EQ(result[1], 1); 
    EXPECT_EQ(result[2], 3); 
    EXPECT_EQ(result[3], 2); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
