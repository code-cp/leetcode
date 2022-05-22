/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 29 15:16:43 2021
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
    shared_ptr<TreeNode<T>> trimBST(shared_ptr<TreeNode<T>> root, T low, T high) {
        if (root == nullptr) return nullptr;
        if (root->val < low) {
            shared_ptr<TreeNode<T>> right = trimBST(root->right, low, high);
            return right;
        }
        if (root->val > high) {
            shared_ptr<TreeNode<T>> left = trimBST(root->left, low, high);
            return left;
        }
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> trimBST(shared_ptr<TreeNode<T>> root, T low, T high) {
        if (root == nullptr) return root; 
        // move root to [L, R]
        while (root != nullptr && (root->val < low || root->val > high)) {
            if (root->val < low) root = root->right; 
            else root = root->left; 
        }
        shared_ptr<TreeNode<T>> cur = root; 
        while (cur != nullptr) {
            while (cur->left && cur->left->val < low) {
                cur->left = cur->left->right; 
            }
            cur = cur->left; 
        }
        cur = root; 

        while (cur != nullptr) {
            while (cur->right && cur->right->val > high) {
                cur->right = cur->right->left; 
            }
            cur = cur->right; 
        }
        return root; 
    }
};

TEST(Test669, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto left = make_shared<TreeNode<int>>(0);
    auto right = make_shared<TreeNode<int>>(2);
    root->left = left; 
    root->right = right; 
    const int low = 1;
    const int high = 2;

    RecursiveSolution<int> rs;
    auto root1 = rs.trimBST(root, low, high);
    EXPECT_FALSE(root1->left);
    IterativeSolution<int> is;
    auto root2 = is.trimBST(root, low, high);
    EXPECT_FALSE(root2->left);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
