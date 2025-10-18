/*
class Node {
  public:
    int data;
    Node* left;
    Node* right;
    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};
*/

class Solution {
  public:
    void sri(Node* root, vector<int>&v){
        if(root==NULL) return;
        if(root->left) sri(root->left,v);
        v.push_back(root->data);
        if(root->right) sri(root->right,v);
    }
    int findMedian(Node* root) {
        // Code here
        vector<int>v;
        sri(root,v);
        if(v.size()%2==0) return (v[v.size()/2-1]);
        return (v[v.size()/2]);
    }
};