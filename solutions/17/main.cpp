/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov  1 09:18:33 2021
> Description:   
 ************************************************************************/
#include <iostream>
#include <string> 
#include <vector> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
private:
    const string letterMap[10] = {
        "", // 0
        "", // 1
        "abc", // 2
        "def", // 3
        "ghi", // 4
        "jkl", // 5
        "mno", // 6
        "pqrs", // 7
        "tuv", // 8
        "wxyz", // 9
    };
public:
    vector<string> result;
    string path;
    void backtracking(const string& digits, int startId) {
        if (digits.size() == startId) {
            result.push_back(path);
            return;
        }
        int digit = digits[startId] - '0';
        string letters = letterMap[digit];
        for (int i = 0; i < letters.size(); ++i) {
            path.push_back(letters[i]);
            backtracking(digits, startId+1);
            path.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0) return result;
        backtracking(digits, 0);
        return result;
    }
};

TEST(Test17, SimpleTest) {
    const string digits = "23";
    Solution s; 
    vector<string> result = s.letterCombinations(digits);
    for (const auto& r : result) {
        cout << "comb ";
        for (const auto& a : r)
            cout << a;
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
