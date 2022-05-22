#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(m+n)
// space complexity O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        int table[26] = {0}; 
        for (const auto& i : s) {
            table[i - 'a']++; 
        }
        for (const auto& j : t) {
            table[j - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            // note here use != instead of > 
            if (table[i] != 0) 
                return false; 
        }
        return true; 
    }
};

TEST(Test242, SimpleTest) {
    const string s1 = "anagram";
    const string s2 = "nagaram";
    Solution s; 
    EXPECT_EQ(s.isAnagram(s1, s2), true); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}