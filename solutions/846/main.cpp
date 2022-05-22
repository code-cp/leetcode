/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Dec 30 15:30:01 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <algorithm> 
#include <numeric> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        sort(hand.begin(), hand.end());
        vector<int> visited(hand.size(), 0);
        for (int i = 0; i < hand.size()-groupSize+1; ++i) {
            if (visited[i] == 1) continue;
            int cardId = 1;
            int j = i + 1;
            vector<int> cards{i};
            while (j < hand.size() && cardId != groupSize) {
                if (visited[j] != 1 && hand[j] == hand[cards[cards.size()-1]]+1) {
                    cardId++;
                    cards.push_back(j);
                }
                j++;
            }
            if (cardId != groupSize) return false;
            for (auto& c : cards) visited[c] = 1;
        }
        if (accumulate(visited.begin(), visited.end(), 0) != hand.size()) return false;
        return true;
    }
};

TEST(Test846, SimpleTest) {
    vector<int> hand{
        1,2,3,6,2,3,4,7,8
    };
    const int groupSize = 3;
    Solution s; 
    EXPECT_TRUE(s.isNStraightHand(hand, groupSize));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
