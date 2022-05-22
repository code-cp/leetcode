/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Tue Nov  9 14:43:53 2021
> Description:   
 ************************************************************************/
#include <string> 
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> partitionLabels(string s) {
        // record rightmost position for each char
        int hash[27] = {0};
        for (int i = 0; i < s.size(); ++i) {
            hash[s[i] - 'a'] = i;
        }
        vector<int> result;
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.size(); ++i) {
            right = max(right, hash[s[i] - 'a']);
            if (i == right) {
                result.push_back(right - left + 1);
                left = i + 1;
            }
        }
        return result;
    }
};

TEST(Test763, SimpleTest) {
    string s = "ababcbacadefegdehijhklij";
    Solution mySol; 
    vector<int> result = mySol.partitionLabels(s);
    for (auto& r : result)
        cout << r << " ";
    cout << endl;
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
