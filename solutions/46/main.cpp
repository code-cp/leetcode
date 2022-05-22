/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Nov  4 15:02:15 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<int> path; 
    vector<vector<int>> result; 
public:
    void backtracking(vector<int>& nums) {
        // base case 
        if (path.size() == nums.size()) {
            result.push_back(path); 
            return; 
        }
        for (int i = 0; i < nums.size(); ++i) {
            auto it = find(path.begin(), path.end(), nums[i]); 
            if (it != path.end())
                continue; 
            path.push_back(nums[i]); 
            backtracking(nums); 
            path.pop_back(); 
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        backtracking(nums); 
        return result; 
    }
};

TEST(Test46, SimpleTest) {
    vector<int> nums{
        1,2,3
    };
    Solution s; 
    vector<vector<int>> result = s.permute(nums);
    for (auto& nums : result) {
        cout << "permutation ";
        for (auto& n : nums)
            cout << n << " ";
        cout << endl;
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
