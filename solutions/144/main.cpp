#include <vector> 
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T>
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode(): val(0), left(nullptr), right(nullptr) {}
    TreeNode(T x): val(x), left(nullptr), right(nullptr) {}
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right): val(x), 
        left(left), right(right) {}
};

class Solution {
public:
    template <typename T>
    void helper(shared_ptr<TreeNode<T>> node, vector<int>& result) {
        // base condition 
        if (node == nullptr) 
            return;
        // middle 
        result.push_back(node->val); 
        // left  
        helper(node->left, result); 
        // right 
        helper(node->right, result); 
    } 
    template <typename T>
    vector<int> preorderTraversal(shared_ptr<TreeNode<T>> root) {
        vector<int> result; 
        // preorder = middle, left, right 
        helper(root, result); 
        return result; 
    }
};

TEST(Test144, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1); 
    auto right1 = make_shared<TreeNode<int>>(2);
    root->right = right1; 
    auto left2 = make_shared<TreeNode<int>>(3); 
    right1->left = left2; 
    Solution s; 
    vector<int> result = s.preorderTraversal(root);  
    EXPECT_EQ(result[0], 1);
    EXPECT_EQ(result[1], 2);
    EXPECT_EQ(result[2], 3);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}