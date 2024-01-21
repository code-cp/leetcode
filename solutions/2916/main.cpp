using LL = long long; 
LL M = 1e9 + 7; 

class SegTreeNode {
public: 
    SegTreeNode* left = nullptr; 
    SegTreeNode* right = nullptr; 
    int start, end;
    // sum over the range  
    LL info; 
    LL delta; 
    bool tag; 

    // init for [a, b] with val
    SegTreeNode(int a, int b, int val) {
        tag = false; 
        delta = 0; 
        start = a, end = b; 
        if (a == b) {
            info = val; 
            return; 
        } 
        int mid = (b-a)/2+a;
        if (left == nullptr) {
            left = new SegTreeNode(a, mid, val); 
            right = new SegTreeNode(mid+1, b, val); 
            info = left->info + right->info; 
        } 
    }

    void pushDown() {
        if (tag && left != nullptr) {
            left->info += delta * (left->end - left->start + 1); 
            // why +=? because we are not yet updating the levels down 
            left->delta += delta; 
            right->info += delta * (right->end - right->start + 1); 
            // why +=? because we are not yet updating the levels down 
            right->delta += delta; 
            left->tag = true; 
            right->tag = true; 
            tag = 0; 
            delta = 0; 
        }
    }

    // increase [a, b] by val
    void updateRangeBy(int a, int b, int val) {
        // check if [a, b] and [start, end] overlap 
        if (b < start || a > end) return; 
        if (a <= start && b >= end) {
            info += val * (end - start + 1); 
            delta += val; 
            tag = true; 
            return; 
        }
        if (left != nullptr) {
            pushDown(); 
            // val is to be updated this time 
            // delta is the previous values not yet used for update 
            left->updateRangeBy(a, b, val+delta); 
            right->updateRangeBy(a, b, val+delta); 
            delta = 0; 
            tag = false; 
            info = left->info + right->info; 
        }
    }

    // query [a, b] sum 
    LL queryRange(int a, int b) {
        // check overlap 
        if (b < start || a > end) return 0; 
        if (a <= start && b >= end) return info; 
        // if reach here, means need to check the subrange 
        if (left != nullptr) {
            pushDown(); 
            LL res = left->queryRange(a, b) + right->queryRange(a, b); 
            // during pushdown the info can be updated for left, right
            // so also need to update info here 
            info = left->info + right->info; 
            return res; 
        }
        throw std::logic_error("Should not reach here");
    }
};

class Solution {
public:
    int sumCounts(vector<int>& nums) {
        unordered_map<int, int> map; 
        int n = nums.size(); 
        
        // record where element appears previously 
        vector<int> prev(n, -1);
        for (int i = 0; i < n; ++i) {
            if (map.find(nums[i]) != map.end()) {
                prev[i] = map[nums[i]]; 
            } 
            map[nums[i]] = i; 
        }     

        SegTreeNode* root = new SegTreeNode(0, n-1, 0); 

        // dp[i] means all square sum for array end at i 
        vector<LL> dp(n); 
        for (int i = 0; i < n; ++i) {
            int k = prev[i]; 
            dp[i] = (i == 0? 0:dp[i-1]); 
            dp[i] += 2*root->queryRange(k+1, i-1); 
            dp[i] += (i-k-1);
            // count the element itself             
            dp[i] += 1;  
            dp[i] %= M; 

            // nums[i] will contribute in this range 
            root->updateRangeBy(k+1, i, 1); 
        } 

        LL res = 0; 
        for (int i = 0; i < n; ++i) {
            res = (res + dp[i]) % M; 
        }

        return res; 
    }
};