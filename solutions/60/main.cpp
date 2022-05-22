#include <iostream>
#include <string> 
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
private:
    int factorial(int n)
    {
        int result = 1; 
        for (int i = 1; i <= n; ++i)
        {
            result *= i; 
        }
        return result; 
    }

    template<typename S>
    void dfs(S & seq, S & result, int k)
    {        
        // base case 
        if (k == 0)
        {
            result += seq;
            return; 
        }
        
        const int n = seq.size(); 
        int r_fac = factorial(n - 1);
        int kth = k / r_fac; 
        k %= r_fac; 

        auto a = next(seq.begin(), kth); 
        result += *a; 
        seq.erase(a); 

        // recursive call 
        dfs(seq, result, k); 
    }
public:
    string getPermutation(int n, int k) {
        string s(n, '0');
        for (int i = 0; i < n; ++i)
        {
            s[i] += i + 1; 
        }

        string result = ""; 

        // do depth first search with pruning 
        dfs(s, result, k-1); 

        return result; 
    }
};

TEST(Test60, SimpleTest) 
{
    Solution s; 
    const int n = 3; 
    const int k = 3; 
    string result = s.getPermutation(n, k); 
    EXPECT_TRUE(result == "213") << "Wrong answer"; 
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
} 
