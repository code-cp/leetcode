/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Dec 17 14:12:23 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int result = 0;
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 'X') {
                    if (i-1 < 0 || (i-1 >= 0 && board[i-1][j] == '.')) {
                        if (j-1 < 0 || j-1 >= 0 && board[i][j-1] == '.')
                            result++;
                    }
                }
            }
        }
        return result;
    }
};

TEST(Test419, SimpleTest) {
    vector<vector<char>> board{{'X','.','.','X'},{'.','.','.','X'},{'.','.','.','X'}};
    Solution s; 
    EXPECT_EQ(s.countBattleships(board), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
