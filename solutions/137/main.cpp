#include <iostream>
#include <vector>
#include <algorithm>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        const int W = sizeof(int) * 8;  
        for (int i = 0, sum = 0; i < W; ++i)
        {
            sum = 0; 
            for (auto n : nums)
            {
                sum += (n >> i) & 1; 
            }
            result |= (sum % 3) << i; 
        }
        return result; 
    }
};

TEST(Test137, SimpleTest)
{
    vector<int> nums = {0,1,0,1,0,1,99}; 
    Solution s; 
    EXPECT_EQ(s.singleNumber(nums), 99); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
