#include <unordered_set> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    int getSum(int n) {
        int sum = 0; 
        while (n > 0) {
            sum += (n%10) * (n%10); 
            n /= 10; 
        }
        return sum; 
    }
    bool isHappy(int n) {
        unordered_set<int> table;
        while (true) {
            int sum = getSum(n); 
            if (sum == 1) 
                return true; 
            else if (table.find(sum) != table.end())
                return false; 
            else {
                table.insert(sum); 
                n = sum; 
            }
        }
    }
};

TEST(Test202, SimpleTest) {
    const int num = 19; 
    Solution s; 
    bool flag = s.isHappy(num); 
    EXPECT_EQ(flag, true); 
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}