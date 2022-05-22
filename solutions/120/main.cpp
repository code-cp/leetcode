#include <iostream>
#include <vector>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = triangle.size() - 2; i >= 0; --i)
        {
            for (int j = 0; j < i + 1; ++j)
            {
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
            }            
        }
        return triangle[0][0]; 
    }
};

TEST(Test120, SimpleTest)
{
    vector<vector<int> > triangle{ { -1 }, 
                               { 2, 3 }, 
                               { 1, -1, -3} }; 
    Solution s; 
    EXPECT_EQ(s.minimumTotal(triangle), -1) << "wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
