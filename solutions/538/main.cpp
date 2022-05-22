/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Oct 30 10:37:15 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <stack> 
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
class RecursiveSolution {
public:
    T _pre;
    RecursiveSolution() : _pre(0) {}
    void traversal(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return;
        // right, visit, left
        traversal(root->right);
        root->val += _pre;
        _pre = root->val;
        traversal(root->left);
    }
    shared_ptr<TreeNode<T>> convertBST(shared_ptr<TreeNode<T>> root) {
        traversal(root);
        return root;
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> convertBST(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return root;
        stack<shared_ptr<TreeNode<T>>> st;
        shared_ptr<TreeNode<T>> cur = root;
        int pre = 0;
        while (cur != nullptr || !st.empty()) {
            if (cur != nullptr) {
                st.push(cur);
                cur = cur->right;
            }
            else {
                cur = st.top();
                st.pop();
                cur->val += pre;
                pre = cur->val;
                cur = cur->left;
            }
        }
        return root;
    }
};

TEST(Test538, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(0);
    auto right = make_shared<TreeNode<int>>(2);
    root->left = left; 
    root->right = right; 

    RecursiveSolution<int> rs;
    // root = rs.convertBST(root);
    // EXPECT_EQ(root->left->val, 3);
    IterativeSolution<int> is; 
    root = is.convertBST(root);
    EXPECT_EQ(root->left->val, 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
