/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov  1 14:26:49 2021
> Description:   
 ************************************************************************/
#include <iostream> 
#include <vector> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
public:
    void backtracking(const vector<int>& candidates, const int target, const int startId) {
        // prune
        if (target < 0) return;
        // base case
        if (target == 0) {
            result.push_back(path);
            return;
        }
        for (int i = startId; i < candidates.size() && candidates[i] <= target; ++i) {
            path.push_back(candidates[i]);
            backtracking(candidates, target - candidates[i], i);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtracking(candidates, target, 0);
        return result;
    }
};

TEST(Test39, SimpleTest) {
    const int target = 7; 
    vector<int> candidates{
        2, 3, 6, 7
    };

    Solution s; 
    vector<vector<int>> result = s.combinationSum(candidates, target);
    for (auto r : result) {
        const int sum = accumulate(r.begin(), r.end(), decltype(r)::value_type(0));
        EXPECT_EQ(target, sum);
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
