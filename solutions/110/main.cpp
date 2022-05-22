/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Thu Oct 14 21:17:06 2021
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
class IterativeSolution {
public:
    int helper(shared_ptr<TreeNode<T>> node) {
        //post order traversal, left, right, visit 
        if (node == nullptr) return 0;
        int leftDepth = helper(node->left);
        if (leftDepth == -1) return -1;
        int rightDepth = helper(node->right);
        if (rightDepth == -1) return -1;
        int diff = abs(leftDepth - rightDepth);
        if (diff > 1) return -1;
        return 1 + max(leftDepth, rightDepth);
    }
    bool isBalanced(shared_ptr<TreeNode<T>> root) {
        return helper(root) == -1 ? false : true;
    }
};

TEST(Test110, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto node1 = make_shared<TreeNode<int>>(9);
    auto node2 = make_shared<TreeNode<int>>(20);
    auto node3 = make_shared<TreeNode<int>>(15);
    auto node4 = make_shared<TreeNode<int>>(7);

    root->left = node1; 
    root->right = node2; 
    node2->left = node3;
    node2->right = node4;

    IterativeSolution<int> is;
    EXPECT_TRUE(is.isBalanced(root));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
