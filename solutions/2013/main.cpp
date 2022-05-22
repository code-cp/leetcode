/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Jan 26 09:19:57 2022
> Description:   
 ************************************************************************/
#include <memory> 
#include <unordered_map> 
#include <gtest/gtest.h> 

using namespace std; 

typedef unordered_map<int, int> uii;

class DetectSquares {
private:
    unordered_map<int, uii> cnt;
public:
    DetectSquares() {

    }

    void add(vector<int> point) {
        int x = point[0], y = point[1];
        cnt[y][x]++;
    }

    int count(vector<int> point) {
        int result = 0;
        int x1 = point[0], y1 = point[1];
        if (cnt.find(y1) == cnt.end()) return result;
        uii& y1_cnt = cnt[y1];
        for (auto& [y2, y2_cnt] : cnt) {
            if (y2 == y1) continue;
            int d = abs(y2 - y1);
            int x1_y2_cnt = y2_cnt.count(x1) ? y2_cnt[x1] : 0;
            int x2_plus_y1_cnt = y1_cnt.count(x1 + d) ? y1_cnt[x1 + d] : 0;
            int x2_minus_y1_cnt = y1_cnt.count(x1 - d) ? y1_cnt[x1 - d] : 0;
            int x2_plus_y2_cnt = y2_cnt.count(x1 + d) ? y2_cnt[x1 + d] : 0;
            int x2_minus_y2_cnt = y2_cnt.count(x1 - d) ? y2_cnt[x1 - d] : 0;
            result += x1_y2_cnt * x2_plus_y1_cnt * x2_plus_y2_cnt;
            result += x1_y2_cnt * x2_minus_y1_cnt * x2_minus_y2_cnt;
        }
        return result;
    }
};

TEST(Test2013, SimpleTest) {
    shared_ptr<DetectSquares> obj = make_shared<DetectSquares>();
    obj->add({
            3, 10
            });
    obj->add({
            11, 2
            });
    obj->add({
            3, 2
            });
    obj->add({
            11, 2
            });
    EXPECT_EQ(obj->count({
            11, 10
            }), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
