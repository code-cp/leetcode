/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov  8 11:19:26 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b) {
        if (a[0] == b[0]) return a[1] < b[1];
        else return a[0] < b[0];
    }
    int findMinArrowShots(vector<vector<int>>& points) {
        int result = 1;
        if (points.size() == 1) return result;
        sort(points.begin(), points.end(), cmp);
        int maxRange = points[0][1];
        for (int i = 1; i < points.size(); ++i) {
            if (maxRange < points[i][0]) {
                maxRange = points[i][1];
                result++;
            }
            else {
                maxRange = min(maxRange, points[i][1]);
            }
        }
        return result;
    }
};

TEST(Test452, SimpleTest) {
    vector<vector<int>> points{{10,16},{2,8},{1,6},{7,12}};
    Solution s;
    EXPECT_EQ(s.findMinArrowShots(points), 2);
}
