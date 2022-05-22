/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Dec 20 15:11:42 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <unordered_map> 
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int countVowelSubstrings(string word) {
        int result = 0; 
        unordered_map<char, int> umap; 
        umap['a'] = 0;
        umap['e'] = 0;
        umap['i'] = 0; 
        umap['o'] = 0;
        umap['u'] = 0;

        auto checkMap = [&]() {
            for (auto& kv : umap) {
                if (kv.second == 0) return false; 
            }
            return true; 
        };
        auto clearMap = [&]() {
            for (auto& kv : umap) kv.second = 0; 
        };

        for (int i = 0; i < word.size(); ++i) {
            if (umap.find(word[i]) == umap.end()) continue; 
            umap[word[i]]++; 
            for (int j = i+1; j < word.size(); ++j) {
                if (umap.find(word[j]) == umap.end()) break;
                umap[word[j]]++;
                if (checkMap()) result++; 
            }
            clearMap(); 
        }

        return result; 
    }
};

TEST(Test2062, SimpleTest) {
    string word = "cuaieuouac"; 
    Solution s; 
    EXPECT_EQ(s.countVowelSubstrings(word), 7);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
