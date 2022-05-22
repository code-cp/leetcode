#include <vector> 
#include <unordered_set> 
#include <unordered_map> 
#include <algorithm> 
#include <gtest/gtest.h> 

using namespace std; 

class Solution {
public:
    vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        // initialize containers 
        unordered_set<long> lamps_set; 
        unordered_map<int, int> row_count; 
        unordered_map<int, int> col_count; 
        unordered_map<int, int> diag_count; 
        unordered_map<int, int> bdiag_count; 
        
        // add lamps 
        for (const auto& l: lamps) {
            // ref: huahua's video 
            long x = static_cast<long>(l[0]) << 32 | l[1]; 
            lamps_set.insert(x); 
        }
        for (const auto& l: lamps_set) {
            int x = l >> 32; int y = 0 | l;
            row_count[x]++; 
            col_count[y]++; 
            diag_count[x-y]++; 
            bdiag_count[x+y]++; 
        }
        
        
        vector<int> ans; ans.reserve(queries.size()); 
        vector<pair<int, int>> dirs{{-1,-1}, {-1,0}, {-1,1}, {0,-1}, {0,0}, {0,1}, {1,-1}, {1,0}, {1,1}}; 
        for (const auto& q: queries) {
            if (row_count[q[0]] > 0 || col_count[q[1]] > 0 || diag_count[q[0]-q[1]] > 0 || bdiag_count[q[0]+q[1]] > 0) ans.push_back(1); 
            else ans.push_back(0); 

            for (const auto& d: dirs) {
                int x = q[0]+d.first, y = q[1]+d.second; 
                if (x < 0 || x > n-1 || y < 0 || y > n-1) continue; 
                long z = static_cast<long>(x) << 32 | y; 
                if (lamps_set.find(z) != lamps_set.end()) {
                    lamps_set.erase(z); 
                    row_count[x]--; 
                    col_count[y]--; 
                    diag_count[x-y]--; 
                    bdiag_count[x+y]--; 
                }
            }
        }
        return ans; 
    }
};

TEST(Test1001, SimpleTest) {
    const int n = 5; 
    vector<vector<int>> lamps{{0,0}, {4,4}}; 
    vector<vector<int>> queries{{1,1}, {1,0}}; 
    Solution s; 
    auto result = s.gridIllumination(n, lamps, queries);
    vector<int> ans{1,0}; 
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin())); 
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}