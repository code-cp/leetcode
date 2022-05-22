/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Nov  3 17:01:43 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
public:
    void backtracking(vector<int>& nums, int startId) {
        // record the node
        result.push_back(path);
        // base case
        if (startId == nums.size()) {
            return;
        }
        for (int i = startId; i < nums.size(); ++i) {
            path.push_back(nums[i]);
            backtracking(nums, i+1);
            path.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        backtracking(nums, 0);
        return result;
    }
};

TEST(Test78, SimpleTest) {
    vector<int> nums{
        1,2,3
    };
    Solution s; 
    vector<vector<int>> result = s.subsets(nums);
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
