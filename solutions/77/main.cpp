/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 31 10:54:17 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
class Solution {
public:
    vector<vector<T>> result;
    vector<T> path;
    void backtracking(int n, int k, int startIndex) {
        // base case
        if (path.size() == k) {
            result.push_back(path);
            return; 
        }
        for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) {
            path.push_back(i);
            backtracking(n, k, i + 1);
            path.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        // the problem asks for 1...n, so start with 1 instead of 0
        backtracking(n, k, 1);
        return result;
    }
};

TEST(Test77, SimpleTest) {
    const int n = 4; 
    const int k = 2; 
    Solution<int> s; 
    vector<vector<int>> result = s.combine(n, k);  
    for (const auto& m : result) {
        cout << "combination ";
        for (const auto& n : m)
            cout << n; 
        cout << " " << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
