#include <iostream> 
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto slowPtr = nums.begin();
        for (auto fastPtr = nums.begin(); fastPtr < nums.end(); fastPtr++)
        {
            if (*fastPtr != val)
                // *slowPtr++ means *(slowPtr++), where slowPtr++ returns the value of old slowPtr
                // and then increment slowPtr
                *slowPtr++ = *fastPtr;
        }
        return distance(nums.begin(), slowPtr); 
    }
};

TEST(Test27, SimpleTest)
{
    vector<int> nums = {3,2,2,3}; 
    const int val = 3; 
    Solution s; 
    EXPECT_EQ(s.removeElement(nums, val), 2) << "Wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
    
