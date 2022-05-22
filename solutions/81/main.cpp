#include <iostream>
#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        
        // check input 
        if (nums.empty())
            return false; 
        
        int left = 0, mid = 0, right = nums.size() - 1; 
        while (left <= right)
        {
            mid = left + (right - left) / 2; 
            
            // obtain proper range that contains target 
            if (nums[left] < nums[mid])
            {
                if (target < nums[left] || target > nums[mid])
                {
                    left = mid + 1; 
                    continue; 
                }
            }
            else if (nums[mid] < nums[right])
            {
                if (target < nums[mid] || target > nums[right])
                {
                    right = mid - 1; 
                    continue; 
                }
            }
            else 
            {
                if (nums[left] == target)
                    return true; 
                else 
                {
                    ++left;
                    continue; 
                }
            }
            
            // normal binary search 
            if (target == nums[mid])
                return true; 
            else if (target < nums[mid])
                right = mid - 1; 
            else 
                left = mid + 1; 
        }
        
        return false; 
    }
};

TEST(Test81, SimpleTest) 
{
    vector<int> nums = {2,5,6,0,0,1,2};
    int target = 0; 
    Solution s; 
    ASSERT_TRUE(s.search(nums, target)) << "Wrong result"; 
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
