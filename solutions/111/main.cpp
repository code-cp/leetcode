/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Oct 13 14:01:55 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <queue> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
struct TreeNode {
    T val; 
    shared_ptr<TreeNode<T>> left; 
    shared_ptr<TreeNode<T>> right; 
    TreeNode() : val(0), left(nullptr), right(nullptr) {

    };
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {

    };
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : val(x), left(left), right(right) {}
};

template <typename T> 
class RecursiveSolution {
public:
    int helper(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return 0; 
        // post order traveral, left, right, visit 
        int leftDepth = helper(node->left); 
        int rightDepth = helper(node->right); 
        if (leftDepth == 0 && rightDepth != 0) return rightDepth + 1; 
        else if (leftDepth != 0 && rightDepth == 0) return leftDepth + 1; 
        else return min(leftDepth, rightDepth) + 1; 
    }
    int minDepth(shared_ptr<TreeNode<T>> root) {
        return helper(root); 
    }
};

template <typename T> 
class IterativeSolution {
public:
    int minDepth(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0; 
        queue<shared_ptr<TreeNode<T>>> mq; 
        int result = 0; 
        mq.push(root); 
        while (!mq.empty()) {
            result++; 
            const int size = mq.size();
            for (int i = 0; i < size; ++i) {
                shared_ptr<TreeNode<T>> node = mq.front(); 
                mq.pop();
                if (node->left == nullptr && node->right == nullptr) return result; 
                else {
                    if (node->left != nullptr) mq.push(node->left);
                    if (node->right != nullptr) mq.push(node->right); 
                }
            }
        }
        return result; 
    }
};

TEST(Test111, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto node1 = make_shared<TreeNode<int>>(9);
    auto node2 = make_shared<TreeNode<int>>(20);
    auto node3 = make_shared<TreeNode<int>>(15);
    auto node4 = make_shared<TreeNode<int>>(7);

    root->left = node1; 
    root->right = node2; 
    node2->left = node3;
    node2->right = node4;

    RecursiveSolution<int> rs; 
    EXPECT_EQ(rs.minDepth(root), 2);
    IterativeSolution<int> is; 
    EXPECT_EQ(is.minDepth(root), 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
