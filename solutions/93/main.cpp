/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov  3 16:40:47 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<string> result;
    string path;
public:
    bool isValid(string& s, int start, int end) {
        if (start > end) return false;
        // string begins with 0 is invalid
        if (s[start] == '0' && start != end) return false;
        int num = 0;
        for (int i = start; i <= end; ++i) {
            // has to be digits
            if (s[i] < '0' || s[i] > '9') return false;
            int n = s[i] - '0';
            num = num * 10 + n;
            // has to be smaller than 255
            if (num > 255) return false;
        }
        return true;
    }
    void backtracking(string& s, int startId, int pointNum) {
        // base case
        if (pointNum == 3) {
            if (isValid(s, startId, s.size()-1)) {
                const int preSize = path.size();
                path += s.substr(startId, s.size()-startId+1);
                result.push_back(path);
                path.erase(preSize, s.size()-startId+1);
            }
            return;
        }
        for (int i = startId; i < s.size(); ++i) {
            if (isValid(s, startId, i)) {
                const int preSize = path.size();
                path += s.substr(startId, i-startId+1) + ".";
                pointNum++;
                backtracking(s, i+1, pointNum);
                pointNum--;
                path.erase(preSize, i-startId+2);
            }
            // note, just end this level here
            else break;
        }
    }
    vector<string> restoreIpAddresses(string s) {
        if (s.size() > 12) return result;
        backtracking(s, 0, 0);
        return result;
    }
};

TEST(Test93, SimpleTest) {
    string myStr = "25525511135";
    Solution s;
    vector<string> result = s.restoreIpAddresses(myStr);
    for (auto& r : result)
        cout << r << endl; 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
