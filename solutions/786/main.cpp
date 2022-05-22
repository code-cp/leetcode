/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Nov 28 14:25:41 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        vector<pair<int, int>> fractions;
        for (int i = 0; i < arr.size(); ++i) {
            for (int j = i+1; j < arr.size(); ++j) {
                fractions.emplace_back(arr[i], arr[j]);
            }
        }
        sort(fractions.begin(), fractions.end(), [](const auto& a, const auto& b) {
            return a.first * b.second < b.first * a.second;
        });
        return {fractions[k-1].first, fractions[k-1].second};
    }
};

TEST(Test786, SimpleTest) {
    vector<int> arr{
        1,2,3,5
    };
    vector<int> ans{
        2,5
    };
    const int k = 3;
    Solution s; 
    vector<int> result = s.kthSmallestPrimeFraction(arr, k);
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
