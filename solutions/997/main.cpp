/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Dec 18 09:07:30 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> inDegree(n+1, 0);
        vector<int> outDegree(n+1, 0);
        for (auto& t : trust) {
            inDegree[t[1]]++;
            outDegree[t[0]]++;
        }
        for (int i = 1; i <= n; ++i) {
            if (inDegree[i] == n-1 && outDegree[i] == 0) return i;
        }
        return -1;
    }
};

TEST(Test997, SimpleTest) {
    const int n = 3; 
    vector<vector<int>> trust{
        {
            1, 3
        }, 
        {
            2, 3
        }
    };
    Solution s; 
    EXPECT_EQ(s.findJudge(n, trust), 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
