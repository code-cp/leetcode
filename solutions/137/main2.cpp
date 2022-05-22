#include <iostream>
#include <vector>
#include <algorithm>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int singleNumber(vector<int>& nums) {
        const int W = sizeof(int) * 8; 
        // count[i] means how many times 1 appears at position i 
        int count[W];     
        fill_n(count, W, 0); 
        for (int i = 0; i < nums.size(); ++i)
        {
            for (int j = 0; j < W; ++j)
            {
                count[j] += (nums[i] >> j) & 1; 
                count[j] %= 3; 
            }
        }
        int result = 0; 
        for (int i = 0; i < W; ++i)
        {
            result += (count[i] << i); 
        }
        return result; 
    }
};

TEST(Test137, SimpleTest)
{
    vector<int> nums = {2,2,3,2};
    Solution s; 
    EXPECT_EQ(s.singleNumber(nums), 3);
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
