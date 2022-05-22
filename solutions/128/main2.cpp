#include <iostream>
#include <vector>
#include <unordered_map>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
private:
    int merge(unordered_map<int, int>& map, const int left, const int right)
    {
        int upper = right + map[right] - 1; 
        int lower = left - map[left] + 1; 
        int length = upper - lower + 1; 
        map[upper] = length; 
        map[lower] = length; 
        return length; 
    }
public:
    int longestConsecutive(vector<int>& nums) {
        
        // check input 
        if (nums.empty())
            return 0; 
        
        // record sequences and length 
        unordered_map<int, int> map; 
        
        int max_length = 1; 
        
        for (const auto & num : nums)
        {
            // check if element already visited 
            if (map.find(num) != map.end())
                continue; 
            
            map[num] = 1; 
            
            if (map.find(num - 1) != map.end())
            {
                int l = merge(map, num - 1, num); 
                max_length = max(max_length, l);
            }
            
            if (map.find(num + 1) != map.end())
            {
                int l = merge(map, num, num + 1);
                max_length = max(max_length, l);
            }
        }
        return max_length; 
    }
};

TEST(Test128, SimpleTest)
{
    vector<int> nums = {100,4,200,1,3,2};
    Solution s;
    EXPECT_EQ(s.longestConsecutive(nums), 4) << "Wrong answer"; 
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
} 
