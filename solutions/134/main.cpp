#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(1)
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0, start = -1; 
        for (int i = 0, sum = 0; i < gas.size(); ++i)
        {
            sum += gas[i] - cost[i];
            total += gas[i] - cost[i]; 
            // if cannot go further at i, then set i as start, zero sum 
            if (sum < 0)
            {
                start = i; 
                sum = 0; 
            }
        }
        return total >= 0 ? start + 1 : -1; 
    }
};

TEST(Test134, SimpleTest)
{
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2}; 

    Solution s; 
    EXPECT_EQ(s.canCompleteCircuit(gas, cost), 3); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
