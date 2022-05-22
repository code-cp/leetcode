/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 15 14:49:45 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    static int bitCount(int num) {
        int count = 0;
        while (num) {
            count++;
            num = num & (num - 1);
        }
        return count;
    }
public:
    static bool cmp(int a, int b) {
        int aN = bitCount(a);
        int bN = bitCount(b);
        if (aN == bN) return a < b;
        else return aN < bN;
    }
    vector<int> sortByBits(vector<int>& arr) {
        sort(arr.begin(), arr.end(), cmp);
        return arr;
    }
};

TEST(Test1356, SimpleTest) {
    vector<int> arr{
        0,1,2,3,4,5,6,7,8
    };
    Solution s; 
    vector<int> result = s.sortByBits(arr);
    for (auto& r : result)
        cout << r << " ";
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
