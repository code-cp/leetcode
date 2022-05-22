/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 29 09:20:42 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <algorithm> 
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
class RecursiveSolution {
public:
    shared_ptr<TreeNode<T>> insertIntoBST(shared_ptr<TreeNode<T>> root, T val) {
        if (root == nullptr) {
            root = make_shared<TreeNode<T>>(val);
        }
        else if (val < root->val) root->left = insertIntoBST(root->left, val);
        else root->right = insertIntoBST(root->right, val);
        return root;
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> insertIntoBST(shared_ptr<TreeNode<T>> root, T val) {
        if (root == nullptr) {
            root = make_shared<TreeNode<T>>(val); 
            return root; 
        }
        shared_ptr<TreeNode<T>> cur = root; 
        shared_ptr<TreeNode<T>> parent = root; 
        while (cur != nullptr) {
            parent = cur; 
            cur = cur->val > val ? cur->left : cur->right; 
        }
        shared_ptr<TreeNode<T>> node = make_shared<TreeNode<T>>(val); 
        if (val < parent->val) parent->left = node; 
        else parent->right = node; 
        return root; 
    }
};

TEST(Test701, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(2);
    auto left = make_shared<TreeNode<int>>(1);
    auto right = make_shared<TreeNode<int>>(3);
    root->left = left; 
    root->right = right; 
    const int val = 4;

    RecursiveSolution<int> rs;
    IterativeSolution<int> is;
    auto root1 = rs.insertIntoBST(root, val);
    EXPECT_EQ(root1->right->right->val, val);
    auto root2 = is.insertIntoBST(root, val);
    EXPECT_EQ(root2->right->right->val, val);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
