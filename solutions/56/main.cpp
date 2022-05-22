/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov  9 15:25:23 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        return a[0] < b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() < 2) return intervals;
        sort(intervals.begin(), intervals.end(), cmp);
        vector<vector<int>> result;
        int left = intervals[0][0];
        int right = intervals[0][1];
        for (int i = 1; i < intervals.size(); ++i) {
            if (right >= intervals[i][0]) {
                right = max(right, intervals[i][1]);
            }
            else {
                result.push_back({left, right});
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        result.push_back({left, right});
        return result;
    }
};

TEST(Test56, SimpleTest) {
    vector<vector<int>> intervals{{1,3},{2,6},{8,10},{15,18}};
    Solution s; 
    vector<vector<int>> result = s.merge(intervals);
    for (auto& r : result) {
        for (auto& n : r) 
            cout << n << " ";
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
