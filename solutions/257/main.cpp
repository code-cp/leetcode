/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Fri Oct 15 08:37:53 2021
> Description:   
 ************************************************************************/
#include <string>
#include <vector>
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
    void travPath(shared_ptr<TreeNode<T>> node, vector<int>& path, vector<string>& result) {
	// pre order traversal, visit, left, right
        path.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            string sPath;
            for (const auto& i : path) {
                sPath += to_string(i);
                sPath += "->";
            }
            sPath.resize(sPath.size() - 2);
            result.push_back(sPath);
            return;
        }

        if (node->left != nullptr) {
            travPath(node->left, path, result);
            path.pop_back();
        }
        if (node->right != nullptr) {
            travPath(node->right, path, result);
            path.pop_back();
        }
    }
    vector<string> binaryTreePaths(shared_ptr<TreeNode<T>> root) {
        vector<int> path;
        vector<string> result;
        if (root == nullptr) return result;
        travPath(root, path, result);
        return result;
    }
};

TEST(Test257, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(3);
    auto node3 = make_shared<TreeNode<int>>(5);

    root->left = node1; 
    root->right = node2; 
    node1->right = node3;

    RecursiveSolution<int> is; 
    vector<string> result = is.binaryTreePaths(root);
    EXPECT_EQ(result[0], "1->2->5");
    EXPECT_EQ(result[1], "1->3");
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
