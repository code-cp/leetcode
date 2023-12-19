class Solution {
public: 
    int uniqueLetterString(string s) {
        // count how many scores each element contribute 
        // ie for each element in s, how many times 
        // it is a unique char in a substring 
        int n = s.size(); 
        vector<vector<int>> pos(26); 

        // every triplet is [-1, xxxx, n]
        for (int k = 0; k < 26; k++)
            pos[k].push_back(-1); 
        for (int i = 0; i < n; i++) 
            pos[s[i] - 'A'].push_back(i);
        for (int k = 0; k < 26; k++) 
            pos[k].push_back(n); 

        int res = 0; 
        for (int k = 0; k < 26; k++) {
            // if pos[k] only has -1, n, means k letter didn't appear in s 
            if (pos[k].size() == 2) continue; 
            for (int i = 1; i < pos[k].size()-1; i++) {
                res += (pos[k][i] - pos[k][i-1]) * (pos[k][i+1] - pos[k][i]); 
            }
        } 

        return res; 
    }
}; 