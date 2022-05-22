/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Oct 20 09:35:55 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <queue> 
#include <stack> 
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
class RecursiveSolution {
public:
    shared_ptr<TreeNode<T>> searchBST(shared_ptr<TreeNode<T>> root, int val) {
        if (root == nullptr || root->val == val) return root;
        else if (root->val < val) return searchBST(root->right, val);
        else if (root->val > val) return searchBST(root->left, val);
        return nullptr;
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> searchBST(shared_ptr<TreeNode<T>> root, int val) {
        while (root != nullptr) {
            if (root->val == val) return root;
            else if (root->val < val) root = root->right;
            else if (root->val > val) root = root->left;
        }
        return nullptr;
    }
};

TEST(Test700, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(4);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(7);
    auto node3 = make_shared<TreeNode<int>>(1);
    auto node4 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;
    node1->left = node3; 
    node1->right = node4; 

    const int val = 2;

    RecursiveSolution<int> rs;
    EXPECT_EQ(rs.searchBST(root, val)->val, val);
    IterativeSolution<int> is;
    EXPECT_EQ(is.searchBST(root, val)->val, val);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
