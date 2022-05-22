/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov  1 15:47:39 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <numeric> 
#include <gtest/gtest.h> 
#include <algorithm> 

using namespace std; 

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
public:
    void backtracking(vector<int>& candidates, int target, int startId) {
        // prune
        if (target < 0) return;
        // base case
        if (target == 0) {
            result.push_back(path);
            return;
        }
        for (int i = startId; i < candidates.size(); ++i) {
            // pruning
            if (candidates[i] > target) return;
            // avoid duplicated answer
            if (i > startId && candidates[i] == candidates[i-1]) continue;
            path.push_back(candidates[i]);
            // note, here is not startId+1, but i+1
            backtracking(candidates, target - candidates[i], i+1);
            path.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        backtracking(candidates, target, 0);
        return result;
    }
};

TEST(Test40, SimpleTest) {
    vector<int> candidates{
        10,1,2,7,6,1,5
    };
    const int target = 8; 
    Solution s; 
    vector<vector<int>> result = s.combinationSum2(candidates, target);
    for (auto r : result) {
        int sum = accumulate(r.begin(), r.end(), decltype(r)::value_type(0));
        EXPECT_EQ(sum, target);
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
