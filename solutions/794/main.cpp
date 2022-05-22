/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Dec  8 22:58:06 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    bool checkEmpty(vector<string>& board) {
        for (auto& s : board) {
            for (auto& c : s) {
                if (c != ' ') return false;
            }
        }
        return true;
    }
    bool checkFull(vector<string>& board) {
        for (auto& s : board) {
            for (auto& c : s) {
                if (c == ' ') return false;
            }
        }
        return true;
    }
    bool checkWin(string& s) {
        if (s[0] == s[1] && s[1] == s[2]) {
            if (s[0] == 'X' || s[0] == 'O') return true;
        }
        return false;
    }
    bool shouldEnd(vector<string>& board) {
        string s = "";
        if (checkFull(board)) return true;
        else {
            for (int i = 0; i < 3; ++i) {
                if (checkWin(board[i])) return true;
                else {
                    s+=board[0][i];
                    s+=board[1][i];
                    s+=board[2][i];
                    if (checkWin(s)) return true;
                    s.clear();
                }
            }
            s+=board[0][0];
            s+=board[1][1];
            s+=board[2][2];
            if (checkWin(s)) return true;
            s.clear();
            s+=board[0][2];
            s+=board[1][1];
            s+=board[2][0];
            if (checkWin(s)) return true;
            s.clear();
        }
        return false;
    }
    bool backtracking(vector<string>& boardTemp, char cPre, vector<string>& board) {
        // base case
        if (boardTemp == board) return true;
        if (shouldEnd(boardTemp)) return false;

        // prune
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (boardTemp[i][j] != ' ' && boardTemp[i][j] != board[i][j]) return false;
            }
        }

        char cNext;
        if (cPre == ' ' || cPre == 'O') cNext = 'X';
        else cNext = 'O';

        // backtracking
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                if (boardTemp[i][j] != ' ') continue;
                boardTemp[i][j] = cNext;
                if (backtracking(boardTemp, cNext, board)) return true;
                boardTemp[i][j] = ' ';
            }
        }

        return false;
    }
public:
    bool validTicTacToe(vector<string>& board) {
        if (checkEmpty(board)) return true;
        vector<string> boardTemp(3, "   ");
        return backtracking(boardTemp, ' ', board);
    }
};

TEST(Test794, SimpleTest) {
    vector<string> board{
        "XOX","O O","XOX"
    }; 
    Solution s; 
    EXPECT_TRUE(s.validTicTacToe(board));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
