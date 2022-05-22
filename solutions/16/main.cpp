#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        int result = 0; 
        
        // check input 
        if (nums.size() < 3)
            return result;  
        
        // sort the array, time complexity O(nlogn) 
        sort(nums.begin(), nums.end()); 
        
        int min_gap = INT_MAX;
        
        // time complexity O(n^2) 
        for (auto i = nums.begin(); i < nums.end() - 2; ++i)
        {
            auto j = next(i);
            auto k = prev(nums.end());
            
            while (j < k)
            {
                auto sum = *i + *j + *k; 
                auto gap = abs(sum - target); 
                if (gap < min_gap)
                {
                    min_gap = gap; 
                    result = sum; 
                }
                
                if (sum < target) 
                    ++j;
                else
                    --k; 
            }
        }
        
        return result; 
    }
};

TEST(Test16, SimpleTest)
{
    vector<int> nums = {-1,2,1,-4};
    int target = 1;
    Solution s; 
    EXPECT_EQ(s.threeSumClosest(nums, target), 2) << "Wrong answer"; 
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
