#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

// time complexity O(n^2)
// space complexity O(n^2)
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // note how 2D array is initialized 
        vector<vector<int>> result(n, vector<int>(n, 0)); 
        int startX = 0, startY = 0; 
        int loop = n / 2, mid = n / 2; 
        int count = 1; 
        int offset = 1; 
        int i, j; 
        while (loop--) {
            i = startX; 
            j = startY; 

            // all ranges are [)
            // from left to right 
            for (j = startY; j < startY + n - offset; ++j)
                result[startX][j] = count++; 
            // from up to down 
            for (i = startX; i < startX + n - offset; ++i)
                result[i][j] = count++; 
            // from right to left 
            for (; j > startY; --j)
                result[i][j] = count++; 
            // from bottom to up 
            for (; i > startX; --i)
                result[i][j] = count++; 

            startX++; 
            startY++;
            offset += 2; 
        }

        // fill in the central value 
        if (n % 2) 
            result[mid][mid] = count; 
        
        return result; 
    }
};

TEST(Test59, SimpleTest)
{
    const int n = 3; 
    vector<vector<int>> ans {
        {1,2,3},
        {8,9,4},
        {7,6,5}
    };
    Solution s; 
    vector<vector<int>> result = s.generateMatrix(n);
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
        {
            EXPECT_EQ(ans[i][j], result[i][j]); 
        }
}

int main()
{
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}