#include <iostream>
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        if (nums.empty())
            return -1; 
        
        int left = 0, mid = 0, right = nums.size() - 1; 
        
        while (left <= right)
        {
            mid = left + (right - left) / 2; 
            if (nums[left] <= nums[mid])
            {
                if (nums[left] > target || target > nums[mid])
                {
                    left = mid + 1; 
                    continue; 
                }
            }
            else 
            {
                if (nums[mid] > target || target > nums[right])
                {
                    right = mid - 1; 
                    continue; 
                }
            }
            if (nums[mid] == target)
                return mid; 
            else if (nums[mid] > target)
                right = mid - 1; 
            else 
                left = mid + 1; 
        }
        
        return -1; 
    }
};

TEST(Test33, SimpleTest) {
    vector<int> nums = {4,5,6,7,0,1,2};
    const int target = 0; 
    Solution s; 
    EXPECT_EQ(s.search(nums, target), 4) << "Wrong, expected 4"; 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}
