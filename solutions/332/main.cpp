/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Nov  5 09:20:59 2021
> Description:   
 ************************************************************************/
#include <iostream> 
#include <unordered_map> 
#include <map> 
#include <utility> 
#include <string> 
#include <gtest/gtest.h>

using namespace std; 

class Solution {
private:
    // unordered_map<from, map<to, flight no>>
    unordered_map<string, map<string, int>> targets;
    vector<string> result;
public:
    bool backtracking(vector<vector<string>>& tickets) {
        // base case
        if (result.size() == tickets.size()+1) {
            return true;
        }
        // const string since key in map is not changable
        for (pair<const string, int>& target: targets[result[result.size()-1]]) {
            if (target.second > 0) {
                result.push_back(target.first);
                target.second--;
                // note, need to return here if true
                if (backtracking(tickets)) return true;
                result.pop_back();
                target.second++;
            }
        }
        return false;
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        targets.clear();
        for (const vector<string>& vec : tickets) {
            targets[vec[0]][vec[1]]++;
        }
        result.push_back("JFK");
        bool success = backtracking(tickets);
        return result;
    }
};

TEST(Test332, SimpleTest) {
    vector<vector<string>> tickets; 
    vector<string> ticket1{
        "MUC","LHR"
    };
    vector<string> ticket2{
        "JFK","MUC"
    };
    vector<string> ticket3{
        "SFO","SJC"
    };
    vector<string> ticket4{
        "LHR","SFO"
    };
    tickets.push_back(ticket1);
    tickets.push_back(ticket2);
    tickets.push_back(ticket3);
    tickets.push_back(ticket4);
    Solution s; 
    vector<string> result = s.findItinerary(tickets);
    cout << "itineray ";
    for (auto& r : result) 
        cout << r << " ";
    cout << endl; 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
