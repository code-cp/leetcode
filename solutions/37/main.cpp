/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov  5 11:38:30 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool isValid(const vector<vector<char>>& board, int n, int row, int col, int val) {
        // check row
        for (int i = 0; i < n; i++) {
            if (board[row][i] == val) return false;
        }
        // check col
        for (int i = 0; i < n; i++) {
            if (board[i][col] == val) return false;
        }
        // check block
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = startRow; i < startRow+3; i++)
            for (int j = startCol; j < startCol+3; j++)
                if (board[i][j] == val) return false;
        return true;
    }
    bool backtracking(vector<vector<char>>& board, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != '.') continue;
                for (char k = '1'; k <= '9'; k++) {
                    if (isValid(board, n, i, j, k)) {
                        board[i][j] = k;
                        if (backtracking(board, n)) return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }
    void solveSudoku(vector<vector<char>>& board) {
        const int n = 9;
        backtracking(board, n);
    }
};

TEST(Test37, SimpleTest) {
    vector<vector<char>> board{{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},{'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},{'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},{'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},{'.','.','.','.','8','.','.','7','9'}};
    Solution s; 
    s.solveSudoku(board);
    for (auto& row : board) {
        for (auto& col : row) 
            cout << col << " ";
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
