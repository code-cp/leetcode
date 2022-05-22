/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov 24 09:16:45 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <unordered_set>
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    bool backtracking (const string& s,
            const unordered_set<string>& wordSet,
            vector<int>& memory,
            int startIndex) {
        if (startIndex >= s.size()) {
            return true;
        }
        // 如果memory[startIndex]不是初始值了，直接使用memory[startIndex]的结果
        if (memory[startIndex] != -1) return memory[startIndex];
        for (int i = startIndex; i < s.size(); i++) {
            string word = s.substr(startIndex, i - startIndex + 1);
            if (wordSet.find(word) != wordSet.end() && backtracking(s, wordSet, memory, i + 1)) {
                memory[startIndex] = 1; // 记录以startIndex开始的子串是可以被拆分的
                return true;
            }
        }
        memory[startIndex] = 0; // 记录以startIndex开始的子串是不可以被拆分的
        return false;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<int> memory(s.size(), -1); // -1 表示初始化状态
        return backtracking(s, wordSet, memory, 0);
    }
};

TEST(Test139, SimpleTest) {
    const string s = "leetcode";
    vector<string> wordDict{
        "leet","code"
    };
    Solution sol; 
    EXPECT_TRUE(sol.wordBreak(s, wordDict));
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
