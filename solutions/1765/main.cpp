/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Jan 29 08:47:48 2022
> Description:   
 ************************************************************************/
#include <iostream> 
#include <queue> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

typedef pair<int, int> pii;

class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        // initialize
        int row = isWater.size(), col = isWater[0].size();
        vector<vector<int>> ans(row, vector<int>(col, -1));
        queue<pii> que;
        vector<pii> dirs{{1,0}, {-1,0}, {0,1}, {0,-1}};
        // put water cells in queue
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (isWater[i][j] == 1) {
                    que.push({i, j});
                    ans[i][j] = 0;
                }
            }
        }
        // bfs
        int h = 1;
        while (!que.empty()) {
            int q_size = que.size();
            while (q_size-- > 0) {
                auto coor = que.front();
                int x = coor.first, y = coor.second;
                que.pop();
                for (const auto& d : dirs) {
                    int nx = x + d.first, ny = y + d.second;
                    // out of boundary
                    if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
                    // process unlabled cells
                    if (ans[nx][ny] == -1) {
                        ans[nx][ny] = h;
                        que.push({nx, ny});
                    }
                }
            }
            h++;
        }
        return ans;
    }
};

TEST(Test1765, SimpleTest) {
    vector<vector<int>> isWater{
        {
            0, 1
        },
        {
            0, 0
        }
    };
    Solution s; 
    auto result = s.highestPeak(isWater);
    for (auto& r : result) {
        for (auto& c : r)
            cout << c << " ";
        cout << endl;
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
