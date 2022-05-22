#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

// time complexity O(logn)
// space complexity O(1)
class Solution {
public:
    // use [left, right) instead of [left, right]
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size(); 
        // note that when left == right, [left, right) is not a valid range 
        // so here we use left < right 
        while (left < right)
        {
            // note (right - left) / 2 can also be (right - left) >> 1 
            int middle = left + ((right - left) >> 1);
            if (nums[middle] == target)
                return middle; 
            else if (nums[middle] < target)
                left = middle + 1;
            else 
                // note here right = middle, since range does not include right 
                right = middle; 
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