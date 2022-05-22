/* ************************************************************************
> File Name:     solutions/572/main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 15 10:39:47 2021
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
class RecursiveSolution {
public:
    bool isSameTree(shared_ptr<TreeNode<T>> p, shared_ptr<TreeNode<T>> q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        if (p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
    bool isSubtree(shared_ptr<TreeNode<T>> root, shared_ptr<TreeNode<T>> subRoot) {
        if (root == nullptr && subRoot != nullptr) return false;
        // pre order traversal, visit, left, right
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};

TEST(Test572, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto node1 = make_shared<TreeNode<int>>(4);
    auto node2 = make_shared<TreeNode<int>>(5);
    auto node3 = make_shared<TreeNode<int>>(1);
    auto node4 = make_shared<TreeNode<int>>(2);
    root->left = node1; 
    root->right = node2; 
    node1->left = node3;
    node1->right = node4;

    auto subRoot = make_shared<TreeNode<int>>(4);
    auto node5 = make_shared<TreeNode<int>>(1);
    auto node6 = make_shared<TreeNode<int>>(2);
    subRoot->left = node5;
    subRoot->right = node6;

    RecursiveSolution<int> rs; 
    EXPECT_TRUE(rs.isSubtree(root, subRoot));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
