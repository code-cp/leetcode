/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov  3 14:35:27 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<vector<string>> result;
    vector<string> path;
public:
    bool isPalindrome(const string& s, int start, int end) {
        for (int i = start, j = end; i < j; ++i, --j) {
            if (s[i] != s[j]) return false;
        }
        return true;
    }
    void backtracking(string& s, int startId) {
        // base case
        if (startId == s.size()) {
            result.push_back(path);
            return;
        }
        for (int i = startId; i < s.size(); ++i) {
            if (isPalindrome(s, startId, i)) {
                string str = s.substr(startId, i-startId+1);
                path.push_back(str);
            }
            else continue;
            backtracking(s, i+1);
            path.pop_back();
        }
    }
    vector<vector<string>> partition(string s) {
        backtracking(s, 0);
        return result;
    }
};

TEST(Test131, SimpleTest) {
    const string myStr = "aab";
    Solution s;
    vector<vector<string>> result = s.partition(myStr);
    for (auto r : result) {
        for (auto l : r)
            EXPECT_TRUE(s.isPalindrome(l, 0, l.size()-1));
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
