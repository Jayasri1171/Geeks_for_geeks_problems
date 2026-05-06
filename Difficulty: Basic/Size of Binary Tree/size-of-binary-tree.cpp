/*
Definition for Node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
    void sri(Node* root,int &ans){
        if(root==NULL){
            return ;
        }
        ans=ans+1;
        if(root->left){
            // int tmp=ans+1;
            sri(root->left,ans);   
        }
        if(root->right){
            // int tmp=ans+1;
            sri(root->right,ans);
        }
    }
    int getSize(Node* root) {
        // code here
        int ans=0;
        sri(root,ans);
        return ans;
        
    }
};