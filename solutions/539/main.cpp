/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Jan 18 09:43:55 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std;

class Solution {
private:
    int convertStrToTime(const string& strIn) {
        int timeOut;
        timeOut = 60 * (int(strIn[0] - '0') * 10 + int(strIn[1] - '0')) + (int(strIn[3] - '0') * 10 + int(strIn[4] - '0'));
        return timeOut;
    }
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> timeInts;
        timeInts.reserve(timePoints.size()+1);
        for (const auto& t : timePoints) timeInts.push_back(convertStrToTime(t));
        sort(timeInts.begin(), timeInts.end());
        timeInts.push_back(timeInts[0] + 24*60);
        int minDiff = INT_MAX, diff = 0;
        for (int i = 1; i < timeInts.size(); ++i) {
            diff = timeInts[i] - timeInts[i-1];
            minDiff = diff < minDiff ? diff : minDiff;
        }
        return minDiff;
    }
};

TEST(Test539, SimpleTest) {
    vector<string> timePoints{
        "23:59","00:00"
    };
    Solution s; 
    EXPECT_EQ(s.findMinDifference(timePoints), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
