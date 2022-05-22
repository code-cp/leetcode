#include <iostream> 
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        // check input 
        if (nums.size() < 1)
            return nums.size();
        
        auto cur_iter = nums.begin();
        for (auto i = nums.begin(); i < nums.end(); ++i)
        {
            if (*i != val)
            {
                *cur_iter = *i; 
                ++cur_iter; 
            }
        }
        
        return distance(nums.begin(), cur_iter);
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
    
