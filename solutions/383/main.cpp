#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(m+n)
// space complexity O(1)
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        // note we use array instead of map, since 
        // for map we need RB tree or hash table, that has extra costs 
        int table[26] = {0}; 
        // note table records letters in magazine, not ransom note 
        // since a letter in magazine cannot be used twice 
        for (const auto& l : magazine) {
            table[l - 'a']++; 
        }
        for (const auto& l : ransomNote) {
            if (table[l - 'a'] > 0)
                table[l - 'a']--; 
            else
                return false; 
        }
        return true; 
    }
};

TEST(Test383, SimpleTest) {
    const string ransomNote = "aa"; 
    const string magazine = "aab"; 
    Solution s; 
    bool flag = s.canConstruct(ransomNote, magazine); 
    EXPECT_EQ(flag, true); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}