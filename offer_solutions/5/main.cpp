#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// use double pointer 
// time complexity O(n)
// space complexity O(1)
class Solution {
public:
    string replaceSpace(string s) {
        int count = 0;
        for (const auto& l : s) {
            if (l == ' ')
                count++;
        }
        // allocate space after spaces are replaced by %20
        s.resize(s.size() + count * 2); 
        
        // NOTE, replace from end to start 
        for (int i = s.length() - 1 - count*2, j = s.length() - 1; i < j; --i, --j) {
            if (s[i] != ' ') {
                s[j] = s[i]; 
                continue; 
            }
            else {
                s[j] = '0';
                s[j-1] = '2';
                s[j-2] = '%';
                j-=2; 
            }
        }
        return s; 
    }
};

TEST(Test5, SimpleTest) {
    string in_s = "We are happy."; 
    string ans_s = "We%20are%20happy.";

    Solution s; 
    string out_s = s.replaceSpace(in_s);
    EXPECT_EQ(out_s, ans_s); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();  
}