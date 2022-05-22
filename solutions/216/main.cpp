/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 31 15:06:56 2021
> Description:   
 ************************************************************************/
#include <iostream> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<vector<int>> result; 
    vector<int> path; 
public:
    void backtracking(int k, int n, int startId) {
        // prune invalid sum 
        if (n < 0) return; 
        // base case when we reach leaf node 
        if (k == 0) {
            if (n == 0) result.push_back(path); 
            return; 
        }
        // prune to make sure we can pick k numbers 
        // note here is 9-k+1 instead of 9-(k-path.size())+1
        for (int i = startId; i <= 9-k+1; ++i) {
            path.push_back(i); 
            backtracking(k-1, n-i, i+1); 
            path.pop_back(); 
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        backtracking(k, n, 1); 
        return result; 
    }
};

TEST(Test216, SimpleTest) {
    const int k = 3; 
    const int n = 7; 
    Solution s; 
    vector<vector<int>> result = s.combinationSum3(k, n);
    for (const auto& m : result) {
        cout << "vector ";
        for (const auto& n : m)
            cout << n << " "; 
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
