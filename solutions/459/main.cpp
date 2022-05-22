#include <string> 
#include <gtest/gtest.h> 

using namespace std;

class Solution {
public:
    vector<int> helper(const string& s) {
        vector<int> next(s.size(), 0);
        int j = 0; 
        for (int i = 1; i < s.size(); ++i) {
            while (j > 0 && s[i] != s[j])
                j = next[j-1]; 
            if (s[i] == s[j])
                j++;
            next[i] = j; 
        }
        return next; 
    }
    bool repeatedSubstringPattern(string s) {
        if (s.size() == 0)
            return false; 
        vector<int> next = helper(s);
        const int len = s.size();
        // suppose common pattern length is x, eg for abab, x = 2 
        // then total string length is nx, if string has multiple copies of x 
        // max. common prefix length is mx, then n - m = 1
        // so nx % (n - m)x = 0
        if (next[len - 1] != 0 && len % (len - next[len - 1]) == 0) {
            return true; 
        }
        return false; 
    }
};

TEST(Test459, SimpleTest) {
    const string in_s = "abab"; 
    Solution s; 
    bool flag = s.repeatedSubstringPattern(in_s); 
    EXPECT_TRUE(flag); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}