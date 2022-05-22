#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// reverse the string, then reverse each words back 
// time complexity O(n)
// space complexity O(1)
class Solution {
public:
    void helper(string& s, const int start, const int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            swap(s[i], s[j]);
        }
    }
    string reverseWords(string s) {
        // remove extra spaces 
        int slow = 0, fast = 0; 
        // remove spaces in the beginning 
        while (s[fast] == ' ' && fast < s.length())
            fast++; 
        // remove spaces in the middle 
        for (;fast < s.length(); fast++) {
            if (fast > 1 && s[fast] == ' ' && s[fast - 1] == ' ')
                continue; 
            else
                s[slow++] = s[fast]; 
        }
        // remove the space at the end 
        if (slow > 1 && s[slow - 1] == ' ')
            s.resize(slow - 1);
        else 
            s.resize(slow); 

        // reverse the entire string 
        helper(s, 0, s.length() - 1); 
        // reverse each word back 
        int start = 0, end = 0; 
        bool is_word = false, rev_word = false; 
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != ' ' && !is_word) {
                start = i;
                is_word = true; 
            } 
            if (is_word) {
                if (s[i] == ' ') {
                    end = i - 1;
                    is_word = false; 
                    rev_word = true; 
                }
                else if (i == s.length() - 1) {
                    end = i;  
                    is_word = false;
                    rev_word = true; 
                }
            }
            if (rev_word) {
                helper(s, start, end);
                rev_word = false; 
            }
        }
        return s; 
    }
};

TEST(Test151, SimpleTest) {
    string in_s = "the sky is blue"; 
    string ans_s = "blue is sky the";
    Solution s; 
    string result = s.reverseWords(in_s); 
    EXPECT_EQ(result, ans_s); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}