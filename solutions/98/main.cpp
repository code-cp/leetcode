/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Oct 20 10:28:54 2021
> Description:   
 ************************************************************************/
#include <vector>
#include <algorithm> 
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
    vector<T> nodes_vec;
    void traversal(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return;
        // in order traversal, left, visit, right
        traversal(node->left);
        nodes_vec.push_back(node->val);
        traversal(node->right);
    }
    bool isValidBST(shared_ptr<TreeNode<T>> root) {
        nodes_vec.clear();
        traversal(root);
        auto it = adjacent_find(nodes_vec.begin(), nodes_vec.end(), greater_equal<int>());
        if (it == nodes_vec.end()) return true;
        else return false;
    }
};

TEST(Test98, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(2);
    auto node1 = make_shared<TreeNode<int>>(1);
    auto node2 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;

    RecursiveSolution<int> rs;
    EXPECT_TRUE(rs.isValidBST(root));
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
