/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov  4 11:14:54 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 
#include <iostream> 

using namespace std; 

class Solution {
private: 
    vector<vector<int>> result; 
    vector<int> path; 
public:
    void backtracking(vector<int>&nums, int startId) {
        // collect all nodes 
        result.push_back(path); 
        // base case 
        if (startId == nums.size()) {
            return; 
        }
        for (int i = startId; i < nums.size(); ++i) {
            if (i != startId && nums[i] == nums[i-1]) continue; 
            path.push_back(nums[i]);
            backtracking(nums, i+1); 
            path.pop_back(); 
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        backtracking(nums, 0); 
        return result; 
    }
};

TEST(Test90, SimpleTest) {
    vector<int> nums{
        1,2,2
    };
    Solution s; 
    vector<vector<int>> result = s.subsetsWithDup(nums);
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
