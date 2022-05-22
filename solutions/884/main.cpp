#include <unordered_map>
#include <string> 
#include <gtest/gtest.h> 
#include <algorithm> 

using namespace std; 

class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> umap; 
        std::istringstream iss(s1 + " " + s2);
        for (std::string s; iss >> s; ) 
            umap[s] += 1;  
        vector<string> result;
        // allocate memory to avoid copying
        result.reserve(umap.size()); 
        for (const auto& [w, c] : umap) {
            if (c == 1) result.push_back(w); 
        }
        return result; 
    }
};

TEST(Test884, SimpleTest) {
    string s1 = "this apple is sweet"; 
    string s2 = "this apple is sour"; 
    Solution s; 
    auto result = s.uncommonFromSentences(s1, s2); 
    vector<string> ans{"sweet", "sour"};
    EXPECT_TRUE(equal(result.begin(), result.end(), ans.begin()));
}
