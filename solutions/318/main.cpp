/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov 16 15:21:58 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProduct(vector<string>& words) {
        int result = 0;
        vector<int> wordsInt(words.size(), 0);
        for (int i = 0; i < words.size(); ++i) {
            string w = words[i];
            for (const auto& c : w) {
                wordsInt[i] |= 1 << (c - 'a');
            }
        }
        for (int i = 0; i < words.size(); ++i) {
            for (int j = i+1; j < words.size(); ++j) {
                if (wordsInt[i] & wordsInt[j]) continue;
                else {
                    if (words[i].size() * words[j].size() > result)
                        result = words[i].size() * words[j].size();
                }
            }
        }
        return result;
    }
};

TEST(Test318, SimpleTest) {
    vector<string> words{
        "abcw","baz","foo","bar","xtfn","abcdef"
    };
    Solution s; 
    EXPECT_EQ(s.maxProduct(words), 16);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
