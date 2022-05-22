/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Dec  1 14:52:52 2021
> Description:   
 ************************************************************************/
#include <numeric> 
#include <string> 
#include <queue>  
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    struct cmp{
        bool operator()(const pair<int, int> a, const pair<int, int> b) {
            return a.first < b.first;
        }
    };
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<string> result(score.size(), "");
        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
        for (int i = 0; i < score.size(); ++i) {
            pq.push(pair<int, int>(score[i], i));
        }
        for (int i = 0; i < score.size(); ++i) {
            auto p = pq.top();
            pq.pop();
            switch(i) {
                case 0:
                    result[p.second] = "Gold Medal";
                    break;
                case 1:
                    result[p.second] =  "Silver Medal";
                    break;
                case 2:
                    result[p.second] = "Bronze Medal";
                    break;
                default:
                    result[p.second] = to_string(i+1);
            }
        }
        return result;
    }
};

TEST(Test506, SimpleTest) {
    vector<int> score{
        5,4,3,2,1
    };
    vector<string> ans{
        "Gold Medal","Silver Medal","Bronze Medal","4","5"
    };
    Solution s; 
    vector<string> result = s.findRelativeRanks(score);
    EXPECT_TRUE(equal(ans.begin(), ans.end(), result.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}

