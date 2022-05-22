#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// ref https://zhuanlan.zhihu.com/p/83334559
// since using the next table prevents the brute force matching 
// time complexity is linear 
// time complexity O(n+m)
// space complexity O(m)
class Solution {
public:
    vector<int> helper(const string& s) {
        vector<int> next(s.length(), 0);
        int j = 0; 
        // NOTE, i starts at 1, not 0
        for (int i = 1; i < s.length(); ++i) {
            while (j > 0 && s[i] != s[j]) 
                // this means to find the last longest common substring 
                // and then add the next letter, check whether it is same with letter at i 
                j = next[j - 1]; 
            if (s[i] == s[j]) 
                j++; 
            next[i] = j; 
        } 
        return next; 
    }
    int strStr(string haystack, string needle) {
        if (needle.length() == 0)
            return 0; 

        vector<int> next = helper(needle);
        int j = 0;  
        for (int i = 0; i < haystack.length(); ++i) {
            while (j > 0 && haystack[i] != needle[j])
                j = next[j - 1]; 
            if (haystack[i] == needle[j]) {
                j++; 
                if (j == needle.length())
                    // NOTE, not return i 
                    return i - needle.length() + 1; 
            }
        }
        return -1; 
    }
};

TEST(Test28, SimpleTest) {
    const string haystack = "hello"; 
    const string needle = "ll"; 
    Solution s; 
    int sol = s.strStr(haystack, needle);
    EXPECT_EQ(sol, 2); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}