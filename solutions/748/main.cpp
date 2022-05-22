/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Dec  9 16:57:51 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 
#include <algorithm> 
#include <numeric> 

using namespace std; 

class Solution {
private:
    vector<int> str2token(const string& s) {
        vector<int> result(26, 0);
        for (auto& c : s) {
            if (c == ' ') continue;
            if (c - '0' >= 0 && c - '9' <= 0) continue;
            result[tolower(c)-'a'] += 1;
        }
        return result;
    }
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        string result(20, 'x');
        auto lpRes = str2token(licensePlate);
        for (auto& w : words) {
            auto wRes = str2token(w);
            transform(lpRes.begin(), lpRes.end(), wRes.begin(), wRes.begin(), minus<int>());
            int count = count_if(wRes.begin(), wRes.end(), [](int c){return c > 0;});
            if (count > 0) continue;
            else {
                if (w.size() < result.size()) result = w;
            }
        }
        return result;
    }
};

TEST(Test748, SimpleTest) {
    string licensePlate = "1s3 PSt";
    vector<string> words{
        "step","steps","stripe","stepple"
    };
    Solution s; 
    EXPECT_EQ(s.shortestCompletingWord(licensePlate, words), "steps");
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
