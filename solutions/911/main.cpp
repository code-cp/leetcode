/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Dec 10 20:42:05 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <unordered_map> 
#include <gtest/gtest.h> 

using namespace std; 

class TopVotedCandidate {
private:
    vector<int> times;
    unordered_map<int, int> totalVoteMap;
    unordered_map<int, int> latestVoteMap;
    vector<int> result;
public:
    TopVotedCandidate(vector<int>& persons, vector<int>& times) :
    times(times)
    {
        for (int i = 0; i < times.size(); ++i) {
            if (totalVoteMap.find(persons[i]) == totalVoteMap.end()) totalVoteMap[persons[i]] = 0;
            if (latestVoteMap.find(persons[i]) == latestVoteMap.end()) latestVoteMap[persons[i]] = 0;
            totalVoteMap[persons[i]]++;
            latestVoteMap[persons[i]] = times[i];

            int mvp = 0, mv = INT_MIN;
            for (auto& pv : totalVoteMap) {
                if (pv.second > mv) {
                    mv = pv.second;
                    mvp = pv.first;
                }
                else if (pv.second == mv) {
                    if (latestVoteMap[pv.first] > latestVoteMap[mvp]) mvp = pv.first;
                }
            }
            result.push_back(mvp);
        }
    }

    int q(int t) {
        int left = 0, right = times.size()-1;
        int mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (times[mid] < t) left = mid + 1;
            else if (times[mid] > t) right = mid - 1;
            else return result[mid];
        }
        if (times[mid] > t) mid--;
        return result[mid];
    }
};

TEST(Test911, SimpleTest) {
    vector<int> persons{
        0, 1, 1, 0, 0, 1, 0
    };
    vector<int> times{
        0, 5, 10, 15, 20, 25, 30
    };
    vector<int> queries{
        3, 12, 25, 15, 24, 8
    };
    vector<int> ans{
        0, 1, 1, 0, 0, 1
    };
    TopVotedCandidate s(persons, times); 
    for (int i = 0; i < queries.size(); ++i) {
        EXPECT_EQ(s.q(queries[i]), ans[i]);
    }
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS();
}
