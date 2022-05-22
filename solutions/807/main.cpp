/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Dec 12 11:36:08 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 
#include <algorithm> 
#include <numeric> 

using namespace std; 

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> rowMax(grid.size(), 0);
        vector<int> colMax(grid[0].size(), 0);
        for (int i = 0; i < grid.size(); ++i)
            rowMax[i] = *max_element(grid[i].begin(), grid[i].end());
        for (int i = 0; i < grid[0].size(); ++i) {
            int maxSum = INT_MIN;
            for (int j = 0; j < grid.size(); ++j) {
                if (maxSum < grid[j][i]) maxSum = grid[j][i];
            }
            colMax[i] = maxSum;
        }

        int result = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                result += min(rowMax[i], colMax[j]) - grid[i][j];
            }
        }

        return result;
    }
};

TEST(Test807, SimpleTest) {
    vector<vector<int>> grid = {{3,0,8,4},{2,4,5,7},{9,2,6,3},{0,3,1,0}};
    const int ans = 35; 
    Solution s; 
    EXPECT_EQ(s.maxIncreaseKeepingSkyline(grid), ans);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
