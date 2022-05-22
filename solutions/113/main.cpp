/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sun Oct 17 10:27:31 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <vector> 
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
class Solution {
private:
    vector<vector<int>> result;
public:
    void traversal(shared_ptr<TreeNode<T>> node, int sum, vector<int>& path) {
        if (node == nullptr) return;
        // pre order, visit, left, right
        if (node->left == nullptr && node->right == nullptr) {
            if (node->val == sum) {
                result.push_back(path);
            }
            return;
        }
        if (node->left != nullptr) {
            // back tracking
            path.push_back(node->left->val);
            traversal(node->left, sum - node->val, path);
            path.pop_back();
        }
        if (node->right != nullptr) {
            // back tracking
            path.push_back(node->right->val);
            traversal(node->right, sum - node->val, path);
            path.pop_back();
        }
        return;
    }
    vector<vector<int>> pathSum(shared_ptr<TreeNode<T>> root, int targetSum) {
        if (root == nullptr) return result;
        vector<int> path;
        path.push_back(root->val);
        traversal(root, targetSum, path);
        return result;
    }
};

TEST(Test113, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;

    Solution<int> s; 
    vector<vector<int>> result = s.pathSum(root, 3);
    EXPECT_EQ(result[0][0], 1);
    EXPECT_EQ(result[0][1], 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
