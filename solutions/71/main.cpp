/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Jan  6 11:11:21 2022
> Description:   
 ************************************************************************/
#include <string> 
#include <stack> 
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        stringstream ss(path);
        string item;
        while (getline(ss, item, '/')) {
            if (item == "." or item == "") continue;
            if (item == "..") {
                if (st.size() > 0) st.pop();
                continue;
            }
            st.push(item);
        }
        if (st.empty()) return "/";
        string result = "";
        while (!st.empty()) {
            result = "/" + st.top() + result;
            st.pop();
        }
        return result;
    }
};

TEST(Test71, SimpleTest) {
    string path = "/a/../../b/../c//.//";
    Solution s; 
    string result = s.simplifyPath(path);
    string ans = "/c";
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
