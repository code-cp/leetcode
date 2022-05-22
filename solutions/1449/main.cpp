#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    string MyStrCmp(const string& lhs, const string& rhs)
    {
        if (lhs.size() > rhs.size())
            return lhs; 
        else if (rhs.size() > lhs.size())
            return rhs; 
        else 
        {
            return lhs > rhs ? lhs : rhs; 
        }
    }
public:
    string largestNumber(vector<int>& cost, int target) {
        // only keep the bigger digit with same cost 
        map<int, int> mp; 
        for (int i = cost.size() - 1; i >= 0; --i)
        {
            if (find_if(mp.begin(), mp.end(), 
                [&cost, i](auto& x)
                {
                    return x.second == cost[i];
                }
            ) == mp.end())
            {
                mp[i+1] = cost[i]; 
            }
        }
        
        string dp[mp.size()+1][target + 1]; 

        dp[0][0] = ""; 
        for (int j = 1; j <= target; ++j)
        {
            dp[0][j] = "#"; 
        }

        for (auto it = mp.begin(); it != mp.end(); ++it)
        {
            int i = distance(mp.begin(), it) + 1; 
            int digit = it->first; 
            int c = it->second; 
            for (int j = 0; j <= target; ++j)
            {
                string a, b; 
                // do not pick ith digit 
                a = dp[i - 1][j]; 
                // pick one more ith digit 
                if (j - c >= 0 && dp[i][j - c] != "#")
                {
                    b = to_string(digit) + dp[i][j - c];
                }
                dp[i][j] = MyStrCmp(a, b); 
            }
        }

        if (dp[mp.size()][target] == "#")
            return "0";
        else 
            return dp[mp.size()][target]; 
    }
};

TEST(Test1449, SimpleTest)
{
    vector<int> cost = {4,3,2,5,6,7,2,5,5}; 
    const int target = 9; 
    Solution s; 
    EXPECT_EQ(s.largestNumber(cost, target), "7772") << "wrong answer";
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
