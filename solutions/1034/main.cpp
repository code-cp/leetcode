/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Dec  6 22:00:35 2021
> Description:   
 ************************************************************************/
#include <queue> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

typedef pair<int, int> rc;

class Solution {
public:
    bool shouldAdd(const vector<vector<int>>& grid, int r, int c, int row, int col, vector<vector<int>>& visited) {
        // check base case
        if (r < 0 || c < 0 || r > grid.size()-1 || c > grid[0].size()-1) return false;
        else if (grid[r][c] != grid[row][col]) return false;
        else if (visited[r][c] != 0) return false;
        // need to prevent adding the same pair in queue
        visited[r][c] = 1;
        return true;
    }
    vector<vector<int>> colorBorder(vector<vector<int>>& grid, int row, int col, int color) {
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), 0));
        queue<pair<int, int>> myQue;
        myQue.emplace(row, col);
        vector<int> dirR{-1, 1, 0, 0};
        vector<int> dirC{0, 0, -1, 1};
        visited[row][col] = 1;

        while (!myQue.empty()) {
            rc& p = myQue.front();
            myQue.pop();
            int r = p.first, c = p.second;

            // do bfs
            for (int k = 0; k < dirR.size(); ++k) {
                int x = r+dirR[k], y = c+dirC[k];
                if (shouldAdd(grid, x, y, row, col, visited))
                    myQue.emplace(x, y);
            }

            if (r == 0 || c == 0 || r == grid.size()-1 || c == grid[0].size()-1) {
                visited[r][c] = 2;
            }
            else {
                for (int k = 0; k < dirR.size(); ++k) {
                    int x = r+dirR[k], y = c+dirC[k];
                    if (grid[x][y] != grid[row][col]) {
                        visited[r][c] = 2;
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (visited[i][j] == 2) grid[i][j] = color;
            }
        }
        return grid;
    }
};

TEST(Test1034, SimpleTest) {
    Solution s; 
    vector<vector<int>> grid{{1,2,2,1,1,1,2},{2,1,1,1,2,2,1},{2,1,1,1,2,1,2},{2,2,1,1,1,1,1},{1,2,2,1,2,1,1}}; 
    int row = 4, col = 5, color = 1; 
    s.colorBorder(grid, row, col, color); 
    for (auto& r : grid) {
        for (auto& c : r)
            cout << c << " "; 
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
