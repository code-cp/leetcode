#include <iostream> 
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int max_profit = 0; 

        // check inputs 
        if (prices.size() < 2)
            return max_profit; 

        int cur_min = prices[0]; 

        for (int i = 1; i < prices.size(); ++i)
        {
            if (prices[i] > cur_min)
            {
                max_profit += prices[i] - cur_min; 
		// 每次卖出都把当前价格当成最小值
                cur_min = prices[i]; 
            }
            else 
            {
                cur_min = min(cur_min, prices[i]); 
            }
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

