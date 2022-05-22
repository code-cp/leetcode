#include <iostream>
#include <vector>
#include <unordered_map>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        unordered_map<int, bool> used; 
        for (const auto & i : nums)
            used[i] = false; 
        
        int longest = 0; 
        
        for (const auto i : nums)
        {
            if (used[i])
                continue; 
            
            int length = 1; 
            
            used[i] = true; 
            
            for (int j = i + 1; used.find(j) != used.end(); ++j)
            {
                used[j] = true; 
                ++length; 
            }
            
            for (int j = i - 1; used.find(j) != used.end(); --j)
            {
                used[j] = true; 
                ++length; 
            }
            
            longest = max(longest, length);
        }
        
        return longest; 
    }
};

TEST(Test128, SimpleTest)
{
    vector<int> nums = {100,4,200,1,3,2};
    Solution s; 
    EXPECT_EQ(s.longestConsecutive(nums), 4) << "Wrong answer"; 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
} 
