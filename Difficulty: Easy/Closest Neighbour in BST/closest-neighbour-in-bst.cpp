/*
class Node {
  public:
    int data;
    Node *left;
    Node *right;

    Node(int x) {
        data = x;
        left = NULL;
        right = NULL;
    }
}; */

class Solution {
  public:
     void sri(Node* root,int &s,int n){
        if(root==NULL) return;
        if(root->data <=n and root->data >= s){
            s=root->data;
        }
        sri(root->left,s,n);
        sri(root->right,s,n);
    }
    int findMaxFork(Node* root, int k) {
        // code here
        int s=0;
        sri(root,s,k);
        if(s<=k and s!=0) return s;
        return -1;
    }
    // int findMaxFork(Node* root, int k) {
    //     // code here
        
    // }
};