/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 21:36:13 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        vector<int> s;
        heights.push_back(0);
        int sum = 0;
        int i = 0;
        while (i < heights.size()) {
            if (s.empty() || heights[i] > heights[s.back()]) {
                s.push_back(i);
                ++i;
            }
            else
            {
                int t = s.back();
                s.pop_back();
                // when s is empty, width must be i, since all previous heights must be smaller than heights[t] 
                sum = max(sum, heights[t] * (s.empty() ? i : i - s.back() - 1));
            }
        }
        return sum;
    }
};

TEST(Test84, SimpleTest) {
    vector<int> heights{
        2,1,5,6,2,3
    };
    Solution s; 
    EXPECT_EQ(s.largestRectangleArea(heights), 10);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
