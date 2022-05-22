#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (x == 0) return 0;  
        double result = 1; 
        // use long long to avoid overflow 
        long long N = n; 
        if (N < 0) {
            x = 1/x;
            N *= -1; 
        } 
        while (N > 0) {
            if (N & 1) {
                N -= 1; 
                result *= x; 
            }
            else {
                N >>= 1; 
                x *= x; 
            }
        } 
        return result; 
    }
};

TEST(Test50, SimpleTest) {
    double x = 2.00000; 
    int n = -2; 
    Solution s; 
    EXPECT_EQ(s.myPow(x, n), 0.25000); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}