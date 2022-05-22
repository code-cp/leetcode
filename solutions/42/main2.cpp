#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int trap(vector<int>& height) {
        const int n = height.size();
        // the index of the highest bar that divides the array 
        auto max_itr = max_element(height.begin(), height.end()); 
        int max = distance(height.begin(), max_itr); 
        
        int water = 0; 
        // compute the amount of water trapped on the left 
        for (int i = 0, peak = 0; i < max; ++i)
        {
            if (height[i] > peak)
                peak = height[i];
            else 
                water += peak - height[i]; 
        }
        // compute the amount of water trapped on the right 
        for (int i = n - 1, top = 0; i > max; --i)
        {
            if (height[i] > top)
                top = height[i];
            else 
                water += top - height[i]; 
        }

        return water; 
    }
};

TEST(Test42, SimpleTest)
{
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    Solution s; 
    EXPECT_EQ(s.trap(height), 6) << "wrong answer";
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
