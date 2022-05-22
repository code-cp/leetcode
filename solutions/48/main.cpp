#include <vector>
#include <iostream> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int n = matrix.size();

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n - i; ++j)
            {
                swap(matrix[i][j], matrix[n - 1 - j][n - 1 - i]);
            }
        }

        for (int i = 0; i < n / 2; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                swap(matrix[i][j], matrix[n - 1 - i][j]);
            }
        }
    }
};

TEST(Test48, SimpleTest)
{
    vector<vector<int>> matrix 
    {
	{1,2,3},
	{4,5,6},
	{7,8,9}
    }; 
    Solution s; 
    s.rotate(matrix); 
    EXPECT_EQ(matrix[0][0], 7) << "Wrong answer"; 
    EXPECT_EQ(matrix[0][1], 4) << "Wrong answer"; 
    EXPECT_EQ(matrix[0][2], 1) << "Wrong answer"; 
}

int main()
{
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}

