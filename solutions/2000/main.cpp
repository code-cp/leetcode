#include <string> 
#include <stack> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    string reversePrefix(string word, char ch) {
        stack<char> st; 
        for (const auto& w : word) {
            st.push(w); 
            if (w == ch) {
                const int n = st.size(); 
                for (int i = 0; i < n; ++i) {
                    word[i] = st.top(); 
                    st.pop(); 
                }
                return word; 
            }
        }
        return word; 
    }
};

TEST(Test2000, SimpleTest) {
    string word = "abcdefd"; 
    char ch = 'd'; 
    Solution s; 
    EXPECT_EQ(s.reversePrefix(word, ch), "dcbaefd"); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}
