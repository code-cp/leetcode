// ref https://walkccc.me/LeetCode/problems/0715/

struct SegmentTreeNode {
    int lo; 
    int hi; 

    bool tracked = false; 

    SegmentTreeNode* left; 
    SegmentTreeNode* right; 

    SegmentTreeNode(
        int lo, 
        int hi,
        bool tracked, 
        SegmentTreeNode* left = nullptr, 
        SegmentTreeNode* right = nullptr 
    ) : lo(lo), 
        hi(hi), 
        tracked(tracked), 
        left(left), 
        right(right)
    {}

    ~SegmentTreeNode() {
        delete left; 
        delete right; 
        left = nullptr; 
        right = nullptr; 
    }
}; 

class SegmentTree {
public:
    // explicit prevents implicit parameter type conversion 
    explicit SegmentTree(): root(make_unique<SegmentTreeNode>(0, 1e9, false)) {}

    void addRange(int i, int j) {
        update(root.get(), i, j, true);
    }

    bool queryRange(int i, int j) {
        return query(root.get(), i, j); 
    }

    void removeRange(int i, int j) {
        update(root.get(), i, j, false); 
    }

private: 
    std::unique_ptr<SegmentTreeNode> root; 

    void update(SegmentTreeNode* root, int i, int j, bool tracked) {
        if (root->lo == i && root->hi == j) {
            root->tracked = tracked; 
            root->left = nullptr; 
            root->right = nullptr;  
            return; 
        }

        const int mid = root->lo + (root->hi - root->lo) / 2; 

        if (root->left == nullptr) {
            root->left = new SegmentTreeNode(root->lo, mid, root->tracked); 
            root->right = new SegmentTreeNode(mid+1, root->hi, root->tracked); 
        }

        if (j <= mid) {
            update(root->left, i, j, tracked); 
        } else if (i> mid) {
            update(root->right, i, j, tracked); 
        } else {
            update(root->left, i, mid, tracked); 
            update(root->right, mid+1, j, tracked); 
        }

        root->tracked = root->left->tracked && root->right->tracked;  
    }

    bool query(SegmentTreeNode* root, int i, int j) {
        if (root->lo == i && root->hi == j) return root->tracked; 

        // check if root has left child, if not, then means root node is not expanded 
        // if it does not have left child, then it does not have right child either 
        // ie root is [1, 10], want to check [2, 3] 
        if (root->left == nullptr) return root->tracked; 
        // if root has subtrees, then we need to check each subtree 
        const int mid = root->lo + (root->hi - root->lo) / 2; 
        if (j <= mid) return query(root->left, i, j); 
        if (i > mid) return query(root->right, i, j); 
        return query(root->left, i, mid) && query(root->right, mid+1, j);    
    }
}; 

class RangeModule {

public:
    RangeModule() {
         
    }
    
    void addRange(int left, int right) {
        tree.addRange(left, right-1);
    }
    
    bool queryRange(int left, int right) {
        return tree.queryRange(left, right-1); 
    }
    
    void removeRange(int left, int right) {
        tree.removeRange(left, right-1); 
    }

private: 
    SegmentTree tree; 
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */