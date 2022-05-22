/* ************************************************************************
> File Name:     solutions/112/main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 17 09:13:46 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <stack> 
#include <utility> 
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
    bool hasPathSum(shared_ptr<TreeNode<T>> root, int targetSum) {
        // base case
        if (root == nullptr) return false;
        // pre order traversal, visit, left, right
        if (root->left == nullptr && root->right == nullptr) {
            if (root->val == targetSum)
                return true;
            else
                return false;
        }
        bool leftFlag = false, rightFlag = false;
        if (root->left != nullptr)
            leftFlag = hasPathSum(root->left, targetSum - root->val);
        if (root->right != nullptr)
            rightFlag = hasPathSum(root->right, targetSum - root->val);
        return leftFlag || rightFlag;
    }
};

template <typename T> 
class IterativeSolution {
public:
    bool hasPathSum(shared_ptr<TreeNode<T>> root, int targetSum) {
        if (root == nullptr) return false;
        stack<pair<shared_ptr<TreeNode<T>>, int>> st;
        st.push(pair<shared_ptr<TreeNode<T>>, int>(root, root->val));
        while (!st.empty()) {
            pair<shared_ptr<TreeNode<T>>, int> node = st.top();
            st.pop();
            // pre order, visit, left, right
            if (node.first->left == nullptr && node.first->right == nullptr) {
                if (node.second == targetSum) return true;
            }
            if (node.first->right != nullptr) {
                st.push(pair<shared_ptr<TreeNode<T>>, int>(node.first->right, node.second + node.first->right->val));
            }
            if (node.first->left != nullptr) {
                st.push(pair<shared_ptr<TreeNode<T>>, int>(node.first->left, node.second + node.first->left->val));
            }
        }
        return false;
    }
};

TEST(Test112, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;

    RecursiveSolution<int> rs; 
    EXPECT_TRUE(rs.hasPathSum(root, 3));
    EXPECT_FALSE(rs.hasPathSum(root, 5));
    IterativeSolution<int> is; 
    EXPECT_TRUE(is.hasPathSum(root, 3));
    EXPECT_FALSE(is.hasPathSum(root, 5));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
