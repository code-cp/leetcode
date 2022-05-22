/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Dec 19 13:28:32 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 
#include <algorithm> 

using namespace std; 

class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int hoSize = houses.size(), heSize = heaters.size();
        auto diff = [](int a, int b) {
            return abs(a - b);
        };
        auto validRad = [&](int mid) {
            int i = 0, j = 0;
            while (i < hoSize) {
                if (diff(houses[i], heaters[j]) <= mid) i++;
                else j++;
                if (j >= heSize) return false;
            }
            return true;
        };
        // [l, r]
        int l = 0, r = 1e9, mid = 0;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (validRad(mid)) r = mid - 1;
            else l = mid + 1;
        }
        // NOTE, return l instead of mid
        return l;
    }
};

TEST(Test475, SimpleTest) {
    vector<int> houses{
        1,2,3
    };
    vector<int> heaters{
        2
    };
    Solution s; 
    EXPECT_EQ(s.findRadius(houses, heaters), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
