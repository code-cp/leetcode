#include <memory> 
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

template <typename T> 
class Solution {
public: 
    shared_ptr<TreeNode<T>> invertTree(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return root;
        // pre order traversal 
        // visit, left, right  
        swap(root->left, root->right); 
        invertTree(root->left); 
        invertTree(root->right); 
        return root; 
    }
};

TEST(Test226, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(2); 
    auto left = make_shared<TreeNode<int>>(1);
    auto right = make_shared<TreeNode<int>>(3);
    root->left = left; 
    root->right = right; 
    Solution<int> s; 
    root = s.invertTree(root); 
    EXPECT_EQ(root->val, 2);
    EXPECT_EQ(root->left->val, 3);
    EXPECT_EQ(root->right->val, 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}