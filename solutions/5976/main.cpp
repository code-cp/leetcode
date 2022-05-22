/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Jan  9 16:03:22 2022
> Description:   
 ************************************************************************/
#include <algorithm> 
#include <numeric> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        const int n = matrix.size();
        for (int i = 0; i < n; ++i) {
            vector<int> recordRow(n, 0);
            vector<int> recordCol(n, 0);
            for (int j = 0; j < n; ++j) {
                recordRow[matrix[i][j]-1] = 1;
                recordCol[matrix[j][i]-1] = 1;
            }
            if (accumulate(recordRow.begin(), recordRow.end(), 0) != n) return false;
            if (accumulate(recordCol.begin(), recordCol.end(), 0) != n) return false;
        }
        return true;
    }
};

TEST(Test5976, SimpleTest) {
    vector<vector<int>> matrix{
        {
            1,2,3
        }, 
        {
            3,1,2
        }, 
        {
            2,3,1
        }
    };
    Solution s; 
    EXPECT_TRUE(s.checkValid(matrix));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
