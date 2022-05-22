/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov  5 17:20:59 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int result = 0;
        int cookieId = s.size()-1;
        // for each kid
        for (int i = g.size()-1; i >= 0; --i) {
            if (cookieId >= 0 && g[i] <= s[cookieId]) {
                result++;
                cookieId--;
            }
        }
        return result;
    }
};

TEST(Test455, SimpleTest) {
    vector<int> g{
        1,2,3
    };
    vector<int> s{
        1,1
    };
    Solution mySol; 
    EXPECT_EQ(mySol.findContentChildren(g, s), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
