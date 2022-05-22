/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Wed Oct 20 13:19:04 2021
> Description:   
 ************************************************************************/
#include <algorithm> 
#include <numeric> 
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
    vector<T> vec;
    void traversal(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return;
        traversal(node->left);
        vec.push_back(node->val);
        traversal(node->right);
    }
    int getMinimumDifference(shared_ptr<TreeNode<T>> root) {
        vec.clear();
        traversal(root);
        T diff[vec.size()];
        adjacent_difference(vec.begin(), vec.end(), diff);
        // note, the first element returned by adjacent diff is just the x0, not x1 - x0
        return *min_element(diff+1, diff+vec.size());
    }
};

TEST(Test530, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(4);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(6);
    auto node3 = make_shared<TreeNode<int>>(1);
    auto node4 = make_shared<TreeNode<int>>(3);
    root->left = node1;
    root->right = node2;
    node1->left = node3;
    node1->right = node4;

    RecursiveSolution<int> rs;
    EXPECT_EQ(rs.getMinimumDifference(root), 1);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
