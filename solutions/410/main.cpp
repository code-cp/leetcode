class Solution {
public: 
    void print2DVector(const std::vector<std::vector<long>>& vec) {
        for (const auto& row : vec) {
            for (const auto& element : row) {
                std::cout << element << " ";
            }
            std::cout << std::endl;
        }
    }

    int splitArray(vector<int>& nums, int k) {
        int n = nums.size(); 
        // dp[i][m] divide nums[0..i] into m groups 
        auto dp = vector<vector<long>>(n, vector<long>(k+1, INT_MAX)); 
        
        vector<long> prefix(n, 0); 
        prefix[0] = nums[0];
        for (auto i = 1; i < n; ++i) {
            prefix[i] = prefix[i-1] + nums[i]; 
        }

        for (auto i = 0; i < n; ++i) {
            // cannot divide into 0 group
            dp[i][0] = 0; 
            // if only 1 group, just sum[0..i]
            dp[i][1] = prefix[i]; 
        }

        // must iterate group first 
        for (auto m = 2; m < k+1; ++m) {
            // then iterate num index 
            for (auto i = m-1; i < n; ++i) {
                // then iterate cutoff index 
                for (auto j = 0; j < i; ++j) {
                    // last group is [j+1..i]
                    // cout << "group " << m << " " << "index " << i << "cut at " << j << endl; 
                    dp[i][m] = min(dp[i][m], max(dp[j][m-1], prefix[i] - prefix[j])); 
                }
            }
        }

        // print2DVector(dp); 

        return dp[n-1][k]; 
    }
};


// [1,2,3,4,5], k = 2 

//     0 1  2 groups 
// ----------------
// 1 | 0 1  2147483647 
// 2 | 0 3  2 
// 3 | 0 6  3 
// 4 | 0 10 6 
// 5 | 0 15 9 