#include <iostream>
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int trap(vector<int>& height) {

        const int n = height.size(); 
        vector<int> max_left(n);
        vector<int> max_right(n);  

        for (int i = 1; i < n; ++i)
        {
            // find the max height on the left 
            max_left[i] = max(max_left[i - 1], height[i - 1]);
            // find the max height on the right 
            max_right[n - 1 - i] = max(max_right[n - i], height[n - i]); 
        }

        int sum = 0; 
        for (int i = 0; i < n; ++i)
        {
            int min_height = min(max_left[i], max_right[i]);
            if (min_height > height[i])
            {
                sum += min_height - height[i]; 
            }
        }

        return sum; 
    }
};

TEST(Test42, SimpleTest) 
{
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1}; 
    Solution s; 
    EXPECT_EQ(s.trap(height), 6) << "Wrong answer"; 
}

int main() 
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
