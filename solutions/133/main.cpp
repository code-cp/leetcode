/* ************************************************************************
> File Name:     main.cpp
> Author:        Sean
> Project:    LeetCode
> Created Time:  Sat Dec 18 15:58:20 2021
> Description:   
 ************************************************************************/
#include <vector> 
#include <iostream> 
#include <memory> 
#include <unordered_map> 
#include <gtest/gtest.h> 

using namespace std; 

template <typename T> 
class Node{
public:
    T val; 
    vector<shared_ptr<Node<T>>> neighbors; 
    Node() : val(0) {

    }
    Node(T _val) : val(_val) {

    }
    Node(T _val, vector<shared_ptr<Node<T>>> _neighbors) : val(_val), neighbors(_neighbors) {

    }
};

template <typename T> 
class Solution {
private:
    // old node, cloned node
    unordered_map<shared_ptr<Node<T>>, shared_ptr<Node<T>>> hash;
public:
    shared_ptr<Node<T>> dfs(shared_ptr<Node<T>> node) {
        // base case, return the node if already cloned
        if (hash.find(node) != hash.end())
            return hash[node];
        // else, create the clone and clone edges
        auto nodeClone = make_shared<Node<T>>(node->val);
        hash[node] = nodeClone;
        for (auto& n : node->neighbors)
            nodeClone->neighbors.push_back(dfs(n));
        return hash[node];
    }
    shared_ptr<Node<T>> cloneGraph(shared_ptr<Node<T>> node) {
        if (node == nullptr) return nullptr;
        return dfs(node);
    }
};

TEST(Test133, SimpleTest) {
    auto node1 = make_shared<Node<int>>(1); 
    auto node2 = make_shared<Node<int>>(2); 
    auto node3 = make_shared<Node<int>>(3); 
    auto node4 = make_shared<Node<int>>(4); 
    node1->neighbors.push_back(node2);
    node1->neighbors.push_back(node4);
    node2->neighbors.push_back(node1);
    node2->neighbors.push_back(node3);
    node3->neighbors.push_back(node2);
    node3->neighbors.push_back(node4);
    node4->neighbors.push_back(node1);
    node4->neighbors.push_back(node3);

    Solution<int> s; 
    auto nodeClone = s.cloneGraph(node1); 
    for (auto& n : nodeClone->neighbors) 
        cout << n->val << " ";
}

int main() {
    testing::InitGoogleTest();
    return RUN_ALL_TESTS();
}
