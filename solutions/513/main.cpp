/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Oct 16 09:30:45 2021
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

    }
    TreeNode(T x) : val(x), left(nullptr), right(nullptr) {

    }
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) : val(x), left(left), right(right) {

    }
};

template <typename T> 
class RecursiveSolution {
public:
    int maxLen;
    int leftVal;
    void traversal(shared_ptr<TreeNode<T>> node, int depth) {
        // pre order traversal, visit, left, right
        if (node == nullptr) return;
        if (node->left == nullptr && node->right == nullptr) {
            if (depth > maxLen) {
                leftVal = node->val;
                maxLen = depth;
            }
            return;
        }
        if (node->left != nullptr) {
            depth++;
            traversal(node->left, depth);
            depth--;
        }
        if (node->right != nullptr) {
            depth++;
            traversal(node->right, depth);
            depth--;
        }
    }
    int findBottomLeftValue(shared_ptr<TreeNode<T>> root) {
        maxLen = INT_MIN;
        leftVal = 0;
        traversal(root, 0);
        return leftVal;
    }
};

template <typename T>
class IterativeSolution {
public:
    int findBottomLeftValue(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0;
        queue<shared_ptr<TreeNode<T>>> mq;
        mq.push(root);
        int result = 0;
        while (!mq.empty()) {
            const int size = mq.size();
            for (int i = 0; i < size; ++i) {
                shared_ptr<TreeNode<T>> node = mq.front();
                mq.pop();
                if (node == nullptr) continue;
                // record the leftmost node of each level
                if (i == 0) result = node->val;
                if (node->left != nullptr) mq.push(node->left);
                if (node->right != nullptr) mq.push(node->right);
            }
        }
        return result;
    }
};

TEST(Test513, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(2);
    auto node1 = make_shared<TreeNode<int>>(1);
    auto node2 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;

    RecursiveSolution<int> rs; 
    EXPECT_EQ(rs.findBottomLeftValue(root), 1);
    IterativeSolution<int> is; 
    EXPECT_EQ(is.findBottomLeftValue(root), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
