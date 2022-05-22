#include <iostream> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    bool check(const char & ch, bool used[9])
    {
        // return true if cell is empty 
        if (ch == '.')
            return true; 
        // return false if number is already used 
        if (used[ch - '1'])
            return false; 
        // otherwise, mark the number as used and return true 
        used[ch - '1'] = true; 
        return true; 
    }
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        const int grid_size = 9; 
        bool used[grid_size];

        for (int i = 0; i < grid_size; ++i)
        {
            fill(used, used + grid_size, false); 
            // check row 
            for (int j = 0; j < grid_size; ++j)
            {
                if (!check(board[i][j], used))
                    return false; 
            }

            fill(used, used + grid_size, false); 

            // check column 
            for (int j = 0; j < grid_size; ++j)
            {
                if (!check(board[j][i], used))
                    return false; 
            }
        }

        // loop all sub grids 
        for (int r = 0; r < sqrt(grid_size); ++r)
        {
            for (int c = 0; c < sqrt(grid_size); ++c)
            {
                fill(used, used + grid_size, false);

                // check each sub grid 
                for (int i = r * sqrt(grid_size); i < r * sqrt(grid_size) + sqrt(grid_size); ++i)
                    for (int j = c * sqrt(grid_size); j < c * sqrt(grid_size) + sqrt(grid_size); ++j)
                        if (!check(board[i][j], used))
                            return false; 
            }
        }

        return true; 
    }
};

TEST(Test36, SimpleTest)
{
    Solution s; 
    std::vector<std::vector<char> > board = {{'5','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'}};

    EXPECT_TRUE(s.isValidSudoku(board)) << "Wrong answer"; 
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
