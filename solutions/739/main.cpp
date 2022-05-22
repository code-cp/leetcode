/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 15 15:22:55 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <stack> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size(), 0);
        stack<int> st;
        st.push(0);
        for (int i = 1; i < temperatures.size(); ++i) {
            if (temperatures[i] <= temperatures[st.top()])
                st.push(i);
            else {
                while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
                    ans[st.top()] = i - st.top();
                    st.pop();
                }
                st.push(i);
            }
        }
        return ans;
    }
};

TEST(Test739, SimpleTest) {
    vector<int> temperatures{
        73,74,75,71,69,72,76,73
    };
    Solution s; 
    vector<int> ans = s.dailyTemperatures(temperatures);
    for (auto& a : ans)
        cout << a << " ";
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
