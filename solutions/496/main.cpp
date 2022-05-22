/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Nov 27 14:55:42 2021
> Description:   
 ************************************************************************/
#include <unordered_map> 
#include <stack> 
#include <algorithm> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> umap;
        for (int i = 0; i < nums2.size(); ++i) {
            auto it = find(nums1.begin(), nums1.end(), nums2[i]);
            if (it != nums1.end())
                umap[i] = it - nums1.begin();
        }
        vector<int> result(nums1.size(), -1);
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums2.size(); ++i) {
            if (nums2[i] > nums2[st.top()]) {
                while (!st.empty() && nums2[st.top()] < nums2[i]) {
                    if (umap.count(st.top()) > 0) {
                        int ind = umap[st.top()];
                        result[ind] = nums2[i];
                    }
                    st.pop();
                }
            }
            st.push(i);
        }
        return result;
    }
};

TEST(Test496, SimpleTest) {
    vector<int> nums1{
        4,1,2
    };
    vector<int> nums2{
        1,3,4,2
    };
    vector<int> ans{
        -1,3,-1
    };
    Solution s; 
    vector<int> result = s.nextGreaterElement(nums1, nums2);
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
