/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Oct 23 08:27:42 2021
> Description:   
 ************************************************************************/
#include <memory> 
#include <unordered_map>
#include <algorithm> 
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
class RecursiveSolution1 {
public:
    T maxCount; 
    T count; 
    shared_ptr<TreeNode<T>> pre; 
    vector<T> result; 

    RecursiveSolution1() : maxCount(0), count(0), pre(nullptr) {}

    void traversal(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return; 
        // in order traversal, left, visit, right 
        traversal(node->left);

        if (pre == nullptr) count = 1; 
        else if (pre->val == node->val) count++; 
        else count = 1; 
        pre = node; 
        if (count == maxCount) result.push_back(node->val); 
        if (count > maxCount) {
            maxCount = count; 
            result.clear(); 
            result.push_back(node->val); 
        }

        traversal(node->right);
        return; 
    }
    vector<T> findMode(shared_ptr<TreeNode<T>> root) {
        result.clear(); 
        traversal(root); 
        return result; 
    }
};

template <typename T>
class RecursiveSolution2 {
public:
    unordered_map<T, T> map; 
    vector<T> result; 
    T count; 
    T maxCount; 

    RecursiveSolution2() : count(0), maxCount(0) {}

    void traversal(shared_ptr<TreeNode<T>> node) {
        if (node == nullptr) return; 
        // pre order traversal, visit, left, right
        map[node->val]++; 
        traversal(node->left);
        traversal(node->right); 
        return; 
    }
    vector<T> findMode(shared_ptr<TreeNode<T>> root) {
        result.clear(); 
        traversal(root);         
        for_each(map.begin(), map.end(), [this](const auto& p) {
            this->count = p.second; 
            if (this->count == this->maxCount) this->result.push_back(p.first);
            if (this->count > this->maxCount) {
                this->maxCount = this->count; 
                this->result.clear();
                this->result.push_back(p.first);
            }
        });
        return result; 
    }
};

TEST(Test501, SimpleTest) {
    auto root = make_shared<TreeNode<int>>(1);
    auto node1 = make_shared<TreeNode<int>>(2);
    auto node2 = make_shared<TreeNode<int>>(2);
    root->right = node1; 
    node1->left = node2;

    RecursiveSolution1<int> rs1; 
    EXPECT_EQ(rs1.findMode(root)[0], 2);
    RecursiveSolution2<int> rs2; 
    EXPECT_EQ(rs2.findMode(root)[0], 2);
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
