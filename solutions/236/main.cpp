/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 24 09:47:15 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {

    }
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {

    }
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : val(x), left(left), right(right) {

    }
}; 

template <typename T> 
class Solution {
public:
    shared_ptr<TreeNode<T>> lowestCommonAncestor(shared_ptr<TreeNode<T>> root, shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (root == nullptr || root == p || root == q) return root; 
        // post order traversal, left, right, visit 
        shared_ptr<TreeNode<T>> left = lowestCommonAncestor(root->left, p, q); 
        shared_ptr<TreeNode<T>> right = lowestCommonAncestor(root->right, p, q); 
        if (left != nullptr && right != nullptr) return root; 
        else if (left != nullptr) return left; 
        else return right; 
    }
};

TEST(Test236, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(0);
    auto left = make_shared<TreeNode<int>>(1);
    auto right = make_shared<TreeNode<int>>(2);
    root->left = left;
    root->right = right;
    Solution<int> s;
    EXPECT_EQ(s.lowestCommonAncestor(root, left, right)->val, 0);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
