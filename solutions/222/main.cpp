/* ************************************************************************
> File Name:     solutions/222/main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Oct 14 15:58:03 2021
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

// time complexity O(logn * logn)
template <typename T>
class Solution {
public:
    int helper(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return 0;
        shared_ptr<TreeNode<T>> left = node->left;
        shared_ptr<TreeNode<T>> right = node->right;
        int leftDepth = 0, rightDepth = 0;
        while (left != nullptr) {
            left = left->left;
            leftDepth++;
        }
        while (right != nullptr) {
            right = right->right;
            rightDepth++;
        }
        if (leftDepth == rightDepth) return (2<<leftDepth) - 1;
        return helper(node->left) + helper(node->right) + 1;
    }
    int countNodes(shared_ptr<TreeNode<T>> root) {
        return helper(root);
    }
};

TEST(Test222, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1); 
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(3);
    auto node3 = make_shared<TreeNode<int>>(4);
    auto node4 = make_shared<TreeNode<int>>(5);
    auto node5 = make_shared<TreeNode<int>>(6);

    root->left = node1; 
    root->right = node2; 
    node1->left = node3;
    node1->right = node4; 
    node2->left = node5;

    Solution<int> s; 
    EXPECT_EQ(s.countNodes(root), 6);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
