#include <iostream> 
#include <vector>
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int lengthOfLongestSubstring(string s) {
        const int ASCII_MAX = 255;
        // to store the index of a character's last appearance 
        int last_idx[ASCII_MAX];
        // to store the current start index  
        int cur_start = 0, max_len = 0; 

        // initialize indices to -1 
        fill(last_idx, last_idx + ASCII_MAX, -1); 

        for (int i = 0; i < s.size(); ++i)
        {
            // check if same characters have appeared twice 
            if (last_idx[s[i]] >= cur_start)
            {
                // update max_len 
                max_len = max(max_len, i - cur_start);
                cur_start = last_idx[s[i]] + 1; 
            }
            // record the position of this character 
            last_idx[s[i]] = i; 
        }

        // obtain the string length of last one 
        max_len = max(max_len, (int)s.size() - cur_start); 

        return max_len; 
    }
};

TEST(Test3, SimpleTest)
{
    string s = "abcabcbb"; 
    Solution los; 
    EXPECT_EQ(los.lengthOfLongestSubstring(s), 3) << "wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}
