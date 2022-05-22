#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <gtest/gtest.h>

using namespace std; 

class Solution {
public:
    // time complexity O(n)
    // space complexity O(n)
    int candy(vector<int>& ratings) {
        const int n = ratings.size();
        vector<int> increment_vec(n);

        for (int i = 1, inc = 1; i < n; ++i)
        {
            if (ratings[i] > ratings[i - 1])
                // note, not ++inc 
                increment_vec[i] = max(inc++, increment_vec[i]);
            else 
                inc = 1; 
        }

        for (int i = n - 2, inc = 1; i >=0; --i)
        {
            if (ratings[i] > ratings[i + 1])
                increment_vec[i] = max(inc++, increment_vec[i]);
            else 
                inc = 1; 
        }

        return accumulate(&increment_vec[0], &increment_vec[0] + n, n);
    } 
};

TEST(Test135, SimpleTest)
{
    vector<int> ratings = {1,0,2};
    Solution s; 
    EXPECT_EQ(s.candy(ratings), 5);
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
