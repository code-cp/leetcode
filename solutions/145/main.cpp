#include <memory>
#include <vector> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : 
        val(x), left(left), right(right) {}
};


class Solution {
public:
    template <typename T> 
    void helper(shared_ptr<TreeNode<T>> node, vector<int>& result) {
        if (node == nullptr) 
            return; 
        // left, right, visit 
        helper(node->left, result); 
        helper(node->right, result);
        result.push_back(node->val); 
    }
    template <typename T> 
    vector<int> postorderTraversal(shared_ptr<TreeNode<T>> root) {
        vector<int> result; 
        helper(root, result);
        return result; 
    }
};

TEST(Test145, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1); 
    auto right1 = make_shared<TreeNode<int>>(2); 
    root->right = right1; 
    auto left2 = make_shared<TreeNode<int>>(3); 
    right1->left = left2; 
    Solution s; 
    vector<int> result = s.postorderTraversal(root); 
    EXPECT_EQ(result[0], 3); 
    EXPECT_EQ(result[1], 2);
    EXPECT_EQ(result[2], 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}