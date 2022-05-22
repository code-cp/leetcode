#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(n)
// space complexity O(1)
class Solution {
public:
    // range is []
    void helper(string& s, int start, int end) {
        for (int i = start, j = end; i < j; ++i, --j) {
            swap(s[i], s[j]);
        }
    }
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.length(); i += 2 * k) {
            if (i + k - 1 <= s.length() - 1) {
                helper(s, i, i + k - 1);
                continue; 
            }
            helper(s, i, s.length() - 1); 
        }
        return s; 
    }
};

TEST(Test541, SimpleTest) {
    const string input_str = "abcdefg"; 
    const int k = 2; 
    Solution s; 
    string result = s.reverseStr(input_str, k); 
    EXPECT_EQ(result, "bacdfeg");
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}