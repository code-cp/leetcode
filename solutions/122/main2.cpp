#include <iostream> 
#include <vector>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0; 
        for (int i = 1; i < prices.size(); ++i)
        {
            int diff = prices[i] - prices[i - 1]; 
            if (diff > 0)
                max_profit += diff; 
        }
        return max_profit; 
    }
};

TEST(Test122, SimpleTest)
{
    vector<int> prices = {7,1,5,3,6,4}; 
    Solution s; 
    EXPECT_EQ(s.maxProfit(prices), 7) << "wrong answer";
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
