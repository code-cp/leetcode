#include <memory> 
#include <vector>
#include <stack> 
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
class Solution {
public:
    vector<T> inorderTraversal(shared_ptr<TreeNode<T>> root) {
        vector<T> result; 
        if (root == nullptr) return result; 
        stack<shared_ptr<TreeNode<T>>> st; 
        st.push(root);
        while (!st.empty()) {
            shared_ptr<TreeNode<T>> node = st.top();
            st.pop();
            if (node != nullptr) { 
                if (node->right != nullptr) st.push(node->right);
                st.push(node); 
                st.push(nullptr); 
                if (node->left != nullptr) st.push(node->left); 
            }
            else {
                node = st.top(); 
                st.pop(); 
                result.push_back(node->val); 
            }
        }
        return result; 
    }
};

TEST(Test94, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto right1 = make_shared<TreeNode<int>>(2);
    root->right = right1; 
    auto left2 = make_shared<TreeNode<int>>(3); 
    right1->left = left2; 
    Solution<int> s; 
    vector<int> result = s.inorderTraversal(root);
    EXPECT_EQ(result[0], 1);
    EXPECT_EQ(result[1], 3);
    EXPECT_EQ(result[2], 2);
}

int main() {
    testing::InitGoogleTest(); 
    return RUN_ALL_TESTS(); 
}