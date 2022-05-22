#include <stack> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool isValid(string s) {
        stack<int> st; 
        for (const auto& l : s) {
            if (l == '(') st.push(')'); 
            else if (l == '[') st.push(']');
            else if (l == '{') st.push('}'); 
            else if (st.empty() || st.top() != l) return false; 
            else st.pop();
        }
        return st.empty(); 
    }
};

TEST(Test20, SimpleTest) {
    Solution s; 
    EXPECT_TRUE(s.isValid("()[]{}"));
    EXPECT_FALSE(s.isValid("([)]"));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}

