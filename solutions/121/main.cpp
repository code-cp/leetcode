#include <iostream> 
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // time complexity O(n)
        // space complexity O(1)

        // check input 
        if (prices.size() < 2)
            return 0; 

        int max_profit = 0; 
        int min_price = prices[0]; 

        for (int i = 1; i < prices.size(); ++i)
        {
            int cur_profit = prices[i] - min_price; 
            if (cur_profit > max_profit)
            {
                max_profit = cur_profit; 
            }

            if (min_price > prices[i])
                min_price = prices[i];
        }

        if (max_profit < 0)
            max_profit = 0; 

        return max_profit; 
    }
};


TEST(Test121, SimpleTest)
{
    vector<int> prices = {7,1,5,3,6,4}; 
    Solution s; 
    EXPECT_EQ(s.maxProfit(prices), 5) << "wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

