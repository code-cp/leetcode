#include <iostream>
#include <vector>
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(m*n)
    // space complexity O(1)
    void setZeroes(vector<vector<int>>& matrix) {
        const size_t m = matrix.size();
        const size_t n = matrix[0].size(); 

        // variables for checking whether zero in row or column 
        bool zero_row = false, zero_col = false;

        // check the first row and column
        for (size_t i = 0; i < n; ++i)
        {
            if (matrix[0][i] == 0)
            {
                zero_row = true; 
                break; 
            }
        }
        for (size_t i = 0; i < m; ++i)
        {
            if (matrix[i][0] == 0)
            {
                zero_col = true; 
                break; 
            }
        }


        // check the entire matrix and use the first row and col to store results 
        for (size_t i = 1; i < m; ++i)
        {
            for (size_t j = 1; j < n; ++j)
            {
                if (matrix[i][j] == 0)
                {
                    matrix[0][j] = 0;
                    matrix[i][0] = 0; 
                } 
            }
        } 

        // set the elements except the first row col to zero 
        for (size_t i = 1; i < m; ++i)
        {
            for (size_t j = 1; j < n; ++j)
            {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0; 
            }
        }
        // set the first row and col to zero 
        if (zero_row)
        {
            for (size_t i = 0; i < n; ++i)
            {
                matrix[0][i] = 0; 
            }
        }
        if (zero_col)
        {
            for (size_t i = 0; i < m; ++i)
            {
                matrix[i][0] = 0; 
            }
        }
    }
};

TEST(Test73, SimpleTest)
{
    vector<vector<int> > matrix{{1,1,1}, 
                           {1,0,1}, 
                           {1,1,1}}; 
    Solution s; 
    s.setZeroes(matrix); 
    auto sum = accumulate(matrix.begin(), matrix.end(), 0, 
	[](auto lhs, const auto & rhs)
	{
	    return accumulate(rhs.begin(), rhs.end(), lhs);
	}); 
    EXPECT_EQ(sum, 4); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
