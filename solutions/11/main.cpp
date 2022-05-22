#include <iostream> 
#include <vector>
#include <iterator>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int maxArea(vector<int>& height) {

        int max_area = 0, cur_area = 0; 
        auto left = height.begin(), right = height.end() - 1; 

        while (left < right)
        {
            cur_area = min(*left, *right) * distance(left, right); 
            max_area = max(max_area, cur_area); 
            if (*left <= *right)
                ++left;
            else
                --right; 
        }

        return max_area; 
    }
};

TEST(Test11, SimpleTest)
{
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    Solution s; 
    EXPECT_EQ(s.maxArea(height), 49) << "wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
