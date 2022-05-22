/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Dec 12 14:48:58 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <algorithm> 
#include <numeric>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        // dp table
        vector<vector<int>> dp(3, vector<int>(nums.size(), 0));
        vector<vector<int>> path(3, vector<int>(nums.size(), 0));
        // initialize
        vector<int> preSum(nums.size(), 0);
        int maxId = 0, maxSum = INT_MIN, sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        preSum[k-1] = sum;
        maxSum = sum;
        dp[0][k-1] = maxSum;
        for (int i = k; i < nums.size(); ++i) {
            sum += nums[i];
            sum -= nums[i-k];
            preSum[i] = sum;
            if (sum > maxSum) {
                maxSum = sum;
                maxId = i-k+1;
            }
            path[0][i] = maxId;
            dp[0][i] = maxSum;
        }
        // traverse dp table
        for (int i = 1; i < 3; ++i) {
            maxSum = INT_MIN;
            for (int j = k*(i+1)-1; j < nums.size(); ++j) {
                int curSum = dp[i-1][j-k] + preSum[j];
                if (curSum > maxSum) {
                    maxSum = curSum;
                    maxId = j-k+1;
                }
                path[i][j] = maxId;
                dp[i][j] = maxSum;
            }
        }
        // find results
        vector<int> result(3, 0);
        result[2] = path[2][path[2].size()-1];
        result[1] = path[1][result[2]-1];
        result[0] = path[0][result[1]-1];

        return result;
    }
};

TEST(Test689, SimpleTesst) {
    vector<int> nums{
        1,2,1,2,6,7,5,1
    };
    const int k = 2; 
    vector<int> ans{
        0,3,5
    };
    Solution s; 
    vector<int> result = s.maxSumOfThreeSubarrays(nums, k);
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
