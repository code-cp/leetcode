#include <stack> 
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st; 
        for (const auto& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                int num1 = st.top(); 
                st.pop();
                int num2 = st.top(); 
                st.pop();
                int result; 
                const char *str = t.c_str();
                switch (*str) {
                    case '+': result = num2 + num1; break; 
                    case '-': result = num2 - num1; break; 
                    case '*': result = num2 * num1; break; 
                    case '/': result = num2 / num1; break; 
                }
                st.push(result); 
            }
            else 
                st.push(stoi(t)); 
        }
        return st.top(); 
    }
};

TEST(Test150, SimpleTest) {
    vector<string> tokens = {"2","1","+","3","*"};
    Solution s; 
    int result = s.evalRPN(tokens);
    EXPECT_EQ(result, 9); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}