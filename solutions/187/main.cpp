class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int n = s.length(); 
        if (n <= 10) return {}; 

        int state = 0; 
        unordered_map<char, int> idx; 
        idx['A'] = 0; idx['C'] = 1; idx['G'] = 2; idx['T'] = 3;

        vector<string> ans; 
        // 0x is base 16 
        // need 2*10 = 20 bits to record each substring 
        // 20 bits are FFFFF in 0x 
        int mask = 0x000FFFFF, record[mask+1]; 
        memset(record, 0, sizeof record); 

        // process the first 10 chars in s 
        for (int i = 0; i < 10; i++) {
            state = state << 2 | idx[s[i]]; 
        }
        ++record[state]; 

        for (int i = 10; i < n; ++i) {
            state = (state << 2 | idx[s[i]]) & mask; 
            if (record[state] == 1) {
                ans.emplace_back(s.substr(i-9, 10)); 
            } 
            ++record[state]; 
        }

        return ans; 
    }
};