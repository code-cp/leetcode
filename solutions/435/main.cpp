/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov  9 13:58:36 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() < 2) return 0;
        sort(intervals.begin(), intervals.end(), cmp);
        int result = 0;
        int maxRange = intervals[0][1];

        for (int i = 1; i < intervals.size(); ++i) {
            if (maxRange > intervals[i][0]) {
                result++;
                maxRange = min(intervals[i][1], maxRange);
            }
            else {
                maxRange = max(maxRange, intervals[i][1]);
            }
        }
        return result;
    }
};

TEST(Test435, SimpleTest) {
    vector<vector<int>> intervals{{1,2},{2,3},{3,4},{1,3}};
    Solution s; 
    EXPECT_EQ(s.eraseOverlapIntervals(intervals), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
