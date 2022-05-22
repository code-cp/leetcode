/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov  4 16:22:26 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <unordered_set> 
#include <gtest/gtest.h> 
#include <iostream> 

using namespace std; 

class Solution {
private:
    vector<int> path;
    vector<vector<int>> result;
public:
    void backtracking(vector<int>& nums, vector<bool>& used) {
        // base case
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }
        unordered_set<int> uset;
        for (int i = 0; i < nums.size(); ++i) {
            // avoid duplicates in the same level
            if (uset.find(nums[i]) != uset.end())
                continue;
            // avoid duplicates for the same element
            if (used[i])
                continue;
            used[i] = true;
            uset.insert(nums[i]);
            path.push_back(nums[i]);
            backtracking(nums, used);
            path.pop_back();
            used[i] = false;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<bool> used(nums.size(), false);
        backtracking(nums, used);
        return result;
    }
};

TEST(Test47, SimpleTest) {
    vector<int> nums{
        1,1,2
    };
    Solution s; 
    vector<vector<int>> result = s.permuteUnique(nums);
    for (auto& num : result) {
        cout << "permute ";
        for (auto& n : num) 
            cout << n << " ";
        cout << endl;
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
