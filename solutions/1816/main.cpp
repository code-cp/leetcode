/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Dec  5 14:35:17 2021
> Description:   
 ************************************************************************/
#include <sstream> 
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<string> split(const string& s, char delim) {
        stringstream ss(s);
        string item;
        vector<string> result;
        while (getline(ss, item, delim)) {
            result.push_back(item);
        }
        return result;
    }
    string truncateSentence(string s, int k) {
        string result;
        auto items = split(s, ' ');
        for (int i = 0; i < k; ++i) {
            result += items[i];
            if (i != k-1) result += " ";
        }
        return result;
    }
};

TEST(Test1816, SimpleTest) {
    string s = "Hello how are you Contestant";
    const int k = 4; 
    string ans = "Hello how are you";
    Solution sol; 
    EXPECT_EQ(sol.truncateSentence(s, k), ans);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
