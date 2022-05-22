/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov  4 14:30:58 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <unordered_set> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
public:
    void backtracking(vector<int>& nums, int startId) {
        // collect all nodes
        if (path.size() > 1)
            result.push_back(path);
        // base case
        if (startId == nums.size()) {
            return;
        }
        // avoid duplicated elements on the same level
        unordered_set<int> uset;
        for (int i = startId; i < nums.size(); ++i) {
            if (!path.empty() && nums[i] < path.back())
                continue;
            if (uset.find(nums[i]) != uset.end())
                continue;
            uset.insert(nums[i]);
            path.push_back(nums[i]);
            backtracking(nums, i+1);
            path.pop_back();
        }
    }
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        backtracking(nums, 0);
        return result;
    }
};

TEST(Test491, SimpleTest) {
    vector<int> nums{
        4,6,7,7
    };
    Solution s; 
    vector<vector<int>> result = s.findSubsequences(nums);
    for (auto& num : result) {
        cout << "subset "; 
        for (auto& n : num)
            cout << n << " ";
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
