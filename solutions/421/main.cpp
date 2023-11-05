struct Trie {
    // left child = 0 
    Trie* left = nullptr; 
    // right child = 1 
    Trie* right = nullptr; 

    Trie() {}
}; 

class Solution {
private: 
    Trie* root = new Trie(); 
    static constexpr int HIGH_BIT = 30; 

public: 
    void add(int num) {
        Trie* cur = root; 
        for (int k = HIGH_BIT; k >= 0; k--) {
            int bit = (num >> k) & 1; 
            if (bit == 0) {
                if (!cur->left) {
                    cur->left = new Trie(); 
                }
                cur = cur->left; 
            } else {
                if (!cur->right) {
                    cur->right = new Trie(); 
                }
                cur = cur->right; 
            }
        }
    }

    int check(int num) {
        // check whether there is a number in the trie whose xor with num is maximum 
        Trie* cur = root; 
        int x = 0; 
        for (int k = HIGH_BIT; k >= 0; k--) {
            // check from highest bit to lowest bit 
            int bit = (num >> k) & 1; 
            if (bit == 0) {
                if (cur->right) {
                    cur = cur->right;
                    // the current bit can be 1, so add 1 
                    // eg checking first bit 
                    // ai = 0, aj = 1, ai xor aj = 1 
                    // x = 0 -> x = 1  
                    x = x * 2 + 1; 
                } else {
                    cur = cur->left; 
                    x *= 2; 
                }
            } else {
                if (cur->left) {
                    cur = cur->left; 
                    x = x * 2 + 1; 
                } else {
                    cur = cur->right; 
                    x *= 2; 
                }
            }
        }
        return x; 
    }

    int findMaximumXOR(vector<int>& nums) {
        int n = nums.size(); 
        int x = 0; 
        for (int i = 1; i < n; i++) {
            add(nums[i-1]); 
            x = max(x, check(nums[i]));
        }
        return x; 
    }
};