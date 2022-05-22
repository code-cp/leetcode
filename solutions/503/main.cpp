/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 16:53:29 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <algorithm> 
#include <stack> 
#include <gtest/gtest.h> 

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result(nums.size(), -1);
        stack<int> st;
        st.push(0);
        // simulate two rounds
        for (int i = 0; i < nums.size()*2; ++i) {
            if (nums[st.top()%nums.size()] < nums[i%nums.size()]) {
                while (!st.empty() && nums[st.top()%nums.size()] < nums[i%nums.size()]) {
                    result[st.top()%nums.size()] = nums[i%nums.size()];
                    st.pop();
                }
            }
            st.push(i);
        }
        return result;
    }
};

TEST(Test503, SimpleTest) {
    vector<int> nums{
        1,2,3,4,3
    };
    vector<int> ans{
        2,3,4,-1,4
    };
    Solution s; 
    vector<int> result = s.nextGreaterElements(nums);
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}
