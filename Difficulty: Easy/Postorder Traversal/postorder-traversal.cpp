/*
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};
*/

class Solution {
  public:
    void sri(Node* root, vector<int>&ans){
        if(root==NULL){
            return;
        }
        if(root->left) sri(root->left,ans);
        if(root->right) sri(root->right,ans);
        ans.push_back(root->data);
    }
    vector<int> postOrder(Node* root) {
        // code here
        vector<int>ans;
        sri(root,ans);
        return ans;
    }
};