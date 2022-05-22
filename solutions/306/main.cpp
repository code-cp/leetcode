/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Jan 10 19:23:46 2022
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<string> nums;
    bool checkNum(const string& n) {
        if (n[0] == '0' && n.size() > 1) return false;
        return true;
    }
    string addStr(const string& n1, const string& n2) {
        string result = "";
        int cur = 0, carry = 0;
        int i = n1.size()-1, j = n2.size()-1;
        while (i >= 0 || j >= 0 || carry > 0) {
            int a = i < 0 ? 0 : n1[i]-'0';
            int b = j < 0 ? 0 : n2[j]-'0';
            cur = a + b + carry;
            carry = cur / 10;
            cur -= carry * 10;
            result = to_string(cur) + result;
            i--;
            j--;
        }
        return result;
    }
public:
    Solution() {
        nums.clear();
    }
    bool backtracking(const string& num, int curStart) {
        // base case
        if (nums.size() >= 3) {
            if (nums[nums.size()-1] != addStr(nums[nums.size()-2], nums[nums.size()-3])) return false;
            else if (curStart == num.size()) return true;
        }
        // backtracking
        for (int curEnd = curStart+1; curEnd <= num.size(); ++curEnd) {
            string curStr = num.substr(curStart, curEnd-curStart);
            // pruning
            if (!checkNum(curStr)) continue;
            nums.push_back(curStr);
            if (backtracking(num, curEnd)) return true;
            nums.pop_back();
        }
        return false;
    }
    bool isAdditiveNumber(string num) {
        return backtracking(num, 0);
    }
};

TEST(Test306, SimpleTest) {
    string num = "112358";
    Solution s; 
    EXPECT_TRUE(s.isAdditiveNumber(num));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
