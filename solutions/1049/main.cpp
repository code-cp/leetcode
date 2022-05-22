#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        const int sum = accumulate(stones.begin(), stones.end(), 0);
        const int target = sum / 2; 
        // size is target + 1 since we want to access dp[target] 
        vector<int> dp(target + 1); 
        // 1D knapsack problem 
        for (const auto & stone : stones)
            for (int i = target; i >= stone; --i)
            {
                // dp[i] stores the maximum amount of stones 
                // dp[i] means do not choose stone, dp[i - stone] + stone means choose stone 
		// i decreases since we only want to use each stone once 
                dp[i] = max(dp[i], dp[i - stone] + stone);
            }
        return sum - 2*dp[target]; 
    }
};

TEST(Test1049, SimpleTest)
{
    vector<int> stones = {2,7,4,1,8,1};
    Solution s; 
    EXPECT_EQ(s.lastStoneWeightII(stones), 1); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
