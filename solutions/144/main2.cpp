#include <stack> 
#include <vector> 
#include <memory> 
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
    vector<T> preorderTraversal(shared_ptr<TreeNode<T>> root) {
        vector<T> result; 
        stack<shared_ptr<TreeNode<T>>> st;  
        if (root == nullptr) return result; 
        st.push(root); 
        while (!st.empty()) {
            shared_ptr<TreeNode<T>> node = st.top();
            st.pop();
            result.push_back(node->val); 
            if (node->right != nullptr) st.push(node->right);
            if (node->left != nullptr) st.push(node->left); 
        }
        return result; 
    }
};

TEST(Test144, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1); 
    auto right1 = make_shared<TreeNode<int>>(2); 
    root->right = right1;
    auto left2 = make_shared<TreeNode<int>>(3); 
    right1->left = left2; 
    // NOTE, should NOT use Solution<int> s() here 
    // ref https://stackoverflow.com/a/49802943
    Solution<int> s;
    vector<int> result = s.preorderTraversal(root); 
    EXPECT_EQ(result[0], 1);
    EXPECT_EQ(result[1], 2);
    EXPECT_EQ(result[2], 3);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS(); 
}