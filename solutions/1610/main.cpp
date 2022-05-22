/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Dec 15 16:23:47 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <cmath> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        int result = 0;
        vector<double> ptsAng;
        ptsAng.reserve(2*points.size());
        // convert origin to person
        int ptsOriNum = 0;
        for (auto& p : points) {
            if (p[0] == location[0] && p[1] == location[1]) ptsOriNum++;
            else {
                p[0] -= location[0];
                p[1] -= location[1];
                ptsAng.push_back(atan2(p[1], p[0]));
            }
        }
        // sort the angles
        sort(ptsAng.begin(), ptsAng.end());
        const int len = ptsAng.size();
        for (int i = 0; i < len; ++i) ptsAng.push_back(ptsAng[i] + 2.0*M_PI);
        // sliding window
        int l = 0;
        double fov = M_PI * angle / 180;
        for (int r = 0; r < ptsAng.size(); ++r) {
            while (ptsAng[r] - ptsAng[l] > fov) l++;
            result = max(result, r - l + 1);
        }
        return result + ptsOriNum;
    }
};

TEST(Test1610, SimpleTest) {
    vector<vector<int>> points{{2,1},{2,2},{3,3}};
    const double angle = 90; 
    vector<int> location{
        1,1
    };
    Solution s; 
    EXPECT_EQ(s.visiblePoints(points, angle, location), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

