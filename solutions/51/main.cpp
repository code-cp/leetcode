/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov  5 10:00:05 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <iostream> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private: 
    vector<vector<string>> result; 
public:
    bool isValid(vector<string>& chessboard, int n, int row, int col) {
        // check col 
        for (int i = 0; i < row; ++i) {
            if (chessboard[i][col] == 'Q') return false; 
        }
        // check row 
        // no need to check row since in each level traversal we only place one Q 
        // check diagonal 
        for (int i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--) {
            if (chessboard[i][j] == 'Q') return false; 
        }
        for (int i = row-1, j = col+1; i >= 0 && j < n; i--, j++) {
            if (chessboard[i][j] == 'Q') return false; 
        }
        return true; 
    }
    void backtracking(vector<string>& chessboard, int n, int row) {
        // base case 
        if (row == n) {
            result.push_back(chessboard); 
        }
        for (int col = 0; col < n; col++) {
            if (isValid(chessboard, chessboard.size(), row, col)) {
                chessboard[row][col] = 'Q'; 
                backtracking(chessboard, n, row+1); 
                chessboard[row][col] = '.'; 
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<string> chessboard(n, string(n, '.')); 
        backtracking(chessboard, n, 0); 
        return result; 
    }
};

TEST(Test51, SimpleTest) {
    const int n = 4; 
    Solution s; 
    vector<vector<string>> result = s.solveNQueens(n);
    for (auto& num : result) {
        cout << "solution ";
        for (auto& rs : num) {
            for (auto& r : rs)
                cout << r << " ";
            cout << ",";
        }
        cout << endl;  
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
