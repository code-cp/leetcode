#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

// time complexity O(logn)
// space complexity O(1)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0; 
        int right = nums.size() - 1; 
        // range is [left, right], is valid when left == right 
        while (left <= right)
        {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] == target)
                return middle; 
            else if (nums[middle] < target)
                left = middle + 1;
            else 
                // since range includes right, should be middle - 1 instead of middle 
                right = middle - 1; 
        }
        return -1; 
    }
};

TEST(TestBinarySearch, SimpleTest)
{
    vector<int> nums = {-1,0,3,5,9,12};
    const int target = 9; 
    Solution s; 
    int ind = s.search(nums, target); 
    EXPECT_EQ(ind, 4);
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}