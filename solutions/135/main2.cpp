#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    int solve(const vector<int>&ratings, vector<int>& f, int i)
    {
        if (f[i] == 0)
        {
            f[i] = 1; 
            if (i > 0 && ratings[i] > ratings[i - 1])
                f[i] = max(f[i], solve(ratings, f, i - 1) + 1); 
            if (i < ratings.size() - 1 && ratings[i] > ratings[i + 1])
                f[i] = max(f[i], solve(ratings, f, i + 1) + 1); 
        }
        return f[i]; 
    }
public:
    // time complexity O(n)
    // space complexity O(n)
    int candy(vector<int>& ratings) {
        vector<int> f(ratings.size());
        int sum = 0; 
        for (int i = 0; i < ratings.size(); ++i)
        {
            sum += solve(ratings, f, i);
        }
        return sum; 
    }
};


TEST(Test135, SimpleTest)
{
    vector<int> ratings = {1,2,2};
    Solution s; 
    EXPECT_EQ(s.candy(ratings), 4); 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
