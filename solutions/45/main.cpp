#include <iostream> 
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(n^2)
// space complexity O(n)
class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> min_jump(nums.size(), 0);
        for (int i = 0; i < nums.size(); ++i)
        {
            for (int j = 1; j <= nums[i] && i + j < nums.size(); ++j)
            {
                if (min_jump[i + j] == 0 || min_jump[j] > min_jump[i] + 1)
                {
                    min_jump[i + j] = min_jump[i] + 1; 
                }
            }
        }

        return min_jump[nums.size() - 1]; 
    }
};

TEST(Test45, SimpleTest)
{
    vector<int> nums = {1,2,3};
    Solution s; 
    EXPECT_EQ(s.jump(nums), 2) << "Wrong answer";
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

