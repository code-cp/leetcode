/* ************************************************************************
> File Name:     solutions/404/main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Oct 16 08:30:27 2021
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
    TreeNode(T x, shared_ptr<TreeNode<T>> left, shared_ptr<TreeNode<T>> right) {

    }
}; 

template <typename T> 
class RecursiveSolution {
public:
    int sumOfLeftLeaves(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0;
        int result = 0;
        // post order traversal, left, right, visit
        int leftSum = sumOfLeftLeaves(root->left);
        int rightSum = sumOfLeftLeaves(root->right);
        if (root->left != nullptr && root->left->left == nullptr && root->left->right == nullptr) result += root->left->val;
        return result + leftSum + rightSum;
    }
};

template <typename T> 
class IterativeSolution {
public:
    int sumOfLeftLeaves(shared_ptr<TreeNode<T>> root) {
        if (root == nullptr) return 0;
        stack<shared_ptr<TreeNode<T>>> st;
        st.push(root);
        int result = 0;
        while (!st.empty()) {
            shared_ptr<TreeNode<T>> node = st.top();
            st.pop();
            if (node == nullptr) continue;
            // pre order traversal, visit, left, right
            if (node->left != nullptr && node->left->left == nullptr && node->left->right == nullptr) result += node->left->val;
            if (node->right != nullptr) st.push(node->right);
            if (node->left != nullptr) st.push(node->left);
        }
        return result;
    }
};

TEST(Test404, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(3);
    auto node1 = make_shared<TreeNode<int>>(9);
    auto node2 = make_shared<TreeNode<int>>(20);
    root->left = node1; 
    root->right = node2; 

    RecursiveSolution<int> rs; 
    EXPECT_EQ(rs.sumOfLeftLeaves(root), 9);
    IterativeSolution<int> is; 
    EXPECT_EQ(is.sumOfLeftLeaves(root), 9);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
