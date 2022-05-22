/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 17 18:35:56 2021
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
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) :
        val(x), left(left), right(right) {}
};

template <typename T> 
class RecursiveSolution {
public:
    shared_ptr<TreeNode<T>> mergeTrees(shared_ptr<TreeNode<T>> root1, shared_ptr<TreeNode<T>> root2) {
        if (root1 == nullptr) return root2;
        if (root2 == nullptr) return root1;
        // pre order, visit, left, right
        shared_ptr<TreeNode<T>> node = make_shared<TreeNode<T>>(0);
        node->val = root1->val + root2->val;
        node->left = mergeTrees(root1->left, root2->left);
        node->right = mergeTrees(root1->right, root2->right);

        return node;
    }
};

template <typename T>
class IterativeSolution {
public:
    shared_ptr<TreeNode<T>> mergeTrees(shared_ptr<TreeNode<T>> root1, shared_ptr<TreeNode<T>> root2) {
        if (root1 == nullptr) return root2;
        if (root2 == nullptr) return root1;
        queue<shared_ptr<TreeNode<T>>> mq;
        mq.push(root1);
        mq.push(root2);
        while (!mq.empty()) {
            const int size = mq.size();
            for (int i = 0; i < size; i+=2) {
                shared_ptr<TreeNode<T>> node1 = mq.front();
                mq.pop();
                shared_ptr<TreeNode<T>> node2 = mq.front();
                mq.pop();
                node1->val += node2->val;

                if (node1->left != nullptr && node2->left != nullptr) {
                    mq.push(node1->left);
                    mq.push(node2->left);
                }
                else if (node2->left != nullptr) node1->left = node2->left;
                if (node1->right != nullptr && node2->right != nullptr) {
                    mq.push(node1->right);
                    mq.push(node2->right);
                }
                else if (node2->right != nullptr) node1->right = node2->right;
            }
        }
        return root1;
    }
};

TEST(Test617, SimpleTest) {
    auto root1 = make_shared<TreeNode<int>>(1);
    auto root2 = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    root2->left = node1;

    RecursiveSolution<int> rs;
    auto root3 = rs.mergeTrees(root1, root2);
    EXPECT_EQ(root3->val, 2);
    EXPECT_EQ(root3->left->val, 2);

    IterativeSolution<int> is; 
    auto root4 = is.mergeTrees(root1, root2);
    EXPECT_EQ(root4->val, 2);
    EXPECT_EQ(root4->left->val, 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
