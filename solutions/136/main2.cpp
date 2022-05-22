#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        return accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
    }
};

TEST(Test136, SimpleTest)
{
    vector<int> nums = {4,1,2,1,2};
    Solution s; 
    EXPECT_EQ(s.singleNumber(nums), 4);
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
