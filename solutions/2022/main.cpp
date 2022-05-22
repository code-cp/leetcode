/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Jan  1 11:16:18 2022
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if (original.size() != m*n) {
            vector<vector<int>> empty;
            return empty;
        };
        vector<vector<int>> result(m, vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            auto start = original.begin()+i*n;
            auto end = original.begin()+(i+1)*n;
            copy(start, end, result[i].begin());
        }
        return result;
    }
};

TEST(Test2022, SimpleTest) {
    vector<int> original{
        1,2,3,4
    };
    const int m = 2, n = 2; 
    Solution s; 
    vector<vector<int>> result = s.construct2DArray(original, m, n); 
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
