/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov  8 09:10:21 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <gtest/gtest.h> 
#include <list> 
#include <iterator> 

using namespace std; 

// time complexity O(nlogn + n^2)
// space complexity O(n)
class VecSolution {
public:
    static bool cmp(const vector<int> a, const vector<int> b) {
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] > b[0];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<vector<int>> que;
        for (int i = 0; i < people.size(); ++i) {
            int position = people[i][1];
            que.insert(que.begin() + position, people[i]);
        }
        return que;
    }
};

// time complexity O(nlogn + n^2)
// space complexity O(n)
class ListSolution {
public:
    static bool cmp(const vector<int> a, const vector<int> b) {
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] > b[0];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), cmp);
        // insert using list is more effective than vector
        list<vector<int>> que;
        for (int i = 0; i < people.size(); ++i) {
            int position = people[i][1];
            list<vector<int>>::iterator it = que.begin();
            while (position--) it++;
            que.insert(it, people[i]);
        }
        return vector<vector<int>>(que.begin(), que.end());
    }
};

TEST(Test406, SimpleTest) {
    vector<vector<int>> people{{7,0},{4,4},{7,1},{5,0},{6,1},{5,2}}; 
    VecSolution vs; 
    ListSolution ls; 
    vector<vector<int>> result1 = vs.reconstructQueue(people); 
    vector<vector<int>> result2 = ls.reconstructQueue(people);
    cout << "using vector "; 
    for (auto& r : result1) {
        for (auto& n : r) 
            cout << n << " ";
        cout << endl; 
    }
    cout << "using list ";
    for (auto& r : result2) {
        for (auto& n : r) {
            cout << n << " ";
        }
        cout << endl; 
    }
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
