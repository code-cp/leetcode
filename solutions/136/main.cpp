#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int singleNumber(vector<int>& nums) {
        int x = 0; 
        for (const auto i : nums)
        {
            x ^= i; 
        }
        return x; 
    }
};

TEST(Test136, SimpleTest)
{
    vector<int> nums = {2,2,1};
    Solution s; 
    EXPECT_EQ(s.singleNumber(nums), 1) << "wrong answer";
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
