/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Mon Nov 29 16:02:06 2021
> Description:   
 ************************************************************************/
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

template <typename T> 
class Solution {
private:
    shared_ptr<TreeNode<T>> pre;
    shared_ptr<TreeNode<T>> node1;
    shared_ptr<TreeNode<T>> node2;
public:
    Solution() : pre(nullptr), node1(nullptr), node2(nullptr) {}
    void traverse(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return;
        // in order traversal
        traverse(node->left);
        if (pre->val > node->val) {
            if (node1 == nullptr) {
                node1 = pre;
            }
            else {
                node2 = node;
            }
        }
        pre = node;
        traverse(node->right);
    }
    void recoverTree(shared_ptr<TreeNode<T>> root) {
        pre = make_shared<TreeNode<T>>(INT_MIN);
        traverse(root);
        if (node2 == nullptr) {
            pre = make_shared<TreeNode<T>>(INT_MIN);
            traverse(root);
        }
        swap(node1->val, node2->val);
    }
};

TEST(Test99, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(3);
    auto right = make_shared<TreeNode<int>>(2);
    root->left = left; 
    left->right = right;
    Solution<int> s; 
    s.recoverTree(root);
    EXPECT_EQ(root->val, 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}


