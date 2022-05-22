#include <stack> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> st; 
        for (const auto& l : s) {
            // note, if the stack container is empty, 
            // top causes undefined behavior
            if (st.empty() || st.top() != l) 
                st.push(l); 
            else  
                st.pop(); 
        }
        string result = ""; 
        while (!st.empty()) {
            result += st.top();
            st.pop(); 
        }
        // the characters poped out are in reverse order
        // note, reverse has no return value, need to 
        // return result 
        reverse(result.begin(), result.end());
        return result;
    }
};

TEST(Test1047, SimpleTest) {
    const string s = "abbaca";
    Solution sol; 
    string result = sol.removeDuplicates(s); 
    EXPECT_EQ(result, "ca"); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}