#include <iostream>
#include <vector> 
#include <unordered_map>
#include <queue> 
#include <string> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
    using PIS = pair<int, string>; 
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map <string, int> um; 
        for (const auto & w : words)
        {
            um[w]++; 
        }

        auto cmp = [](const PIS & p1, const PIS & p2)
        {
            // if two strings have same frequency 
            if (p1.first == p2.first)
                return p1.second < p2.second; 
            return p1.first > p2.first; 
        };

        priority_queue<PIS, vector<PIS>, decltype(cmp)> pg(cmp); 

        for (const auto & [key, value] : um)
        {
            pg.push({value, key}); 
            if (pg.size() > k)
                pg.pop();
        }

        vector<string> ans(k);
        while (!pg.empty())
        {
            ans[--k] = pg.top().second; 
            pg.pop(); 
        }

        return ans; 
    }
};

TEST(Test692, SimpleTest)
{
    vector<string> words = {"i", "love", "leetcode", "i", "love", "coding"}; 
    const int k = 2; 
    Solution s; 
    vector<string> results = s.topKFrequent(words, k); 
    EXPECT_EQ("i", results[0]); 
    EXPECT_EQ("love", results[1]);
}

int main() 
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
