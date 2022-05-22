/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Jan 14 09:32:26 2022
> Description:   
 ************************************************************************/
#include <queue> 
#include <vector> 
#include <gtest/gtest.h> 
#include <algorithm> 
#include <numeric> 

using namespace std; 

class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue<pair<int, pair<int, int>>> pq;
        set<pair<int, int>> visited;
        vector<vector<int>> result;

        pq.push(make_pair(-(nums1[0]+nums2[0]), make_pair(0, 0)));
        visited.insert(make_pair(0, 0));
        while (k > 0 and !pq.empty()) {
            auto next_item = pq.top();
            pq.pop();
            int i = next_item.second.first, j = next_item.second.second;
            result.push_back({nums1[i], nums2[j]});
            k--;
            if (i+1 < nums1.size() && visited.find(make_pair(i+1, j)) == visited.end()) {
                pq.push(make_pair(-(nums1[i+1]+nums2[j]), make_pair(i+1, j)));
                visited.insert(make_pair(i+1, j));
            }
            if (j+1 < nums2.size() && visited.find(make_pair(i, j+1)) == visited.end()) {
                pq.push(make_pair(-(nums1[i]+nums2[j+1]), make_pair(i, j+1)));
                visited.insert(make_pair(i, j+1));
            }
        }
        return result;
    }
};

TEST(Test373, SimpleTest) {
    vector<int> nums1{
        1,7,11
    };
    vector<int> nums2{
        2,4,6
    };
    const int k = 3;
    vector<vector<int>> answer = {
        {
            1, 2
        }, 
        {
            1, 4
        },
        {
            1, 6
        }
    };
    Solution s; 
    vector<vector<int>> result = s.kSmallestPairs(nums1, nums2, k);
    EXPECT_TRUE(equal(result.begin(), result.end(), answer.begin()));
}
