#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// reverse the first n characters
// reverse the rest of characters 
// reverse the entire string 
// time complexity O(n)
// space complexity O(1)
class Solution {
public:
    void helper(string& s, int start, int end) {
        for (int i = start, j = end; i < j; i++, --j) {
            swap(s[i], s[j]);
        }
    }
    string reverseLeftWords(string s, int n) {
        helper(s, 0, n - 1);
        helper(s, n, s.length() - 1); 
        helper(s, 0, s.length() - 1);
        return s;  
    }
};

TEST(Test58, SimpleTest) {
    string in_s = "abcdefg"; 
    const int k = 2; 
    string ans_s = "cdefgab"; 
    Solution s; 
    string sol = s.reverseLeftWords(in_s, k); 
    EXPECT_EQ(sol, ans_s);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}