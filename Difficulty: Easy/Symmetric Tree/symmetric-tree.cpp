/*
class Node {
public:
    int data;
    Node *left, *right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};
*/
class Solution {
  public:
    bool sri(Node* root1, Node* root2){
        if(root1==NULL and root2==NULL){
            return true;
        }
        if(root1==NULL and root2!=NULL){
            return false;
        }
        if(root1!=NULL and root2==NULL){
            return false;
        }
        if(root1->data!=root2->data){
            return false;
        }
        return sri(root1->left,root2->right);
        return sri(root1->right,root2->left);
    }
    bool isSymmetric(Node* root) {
        // Code here
        if(root==NULL){
            return false;
        }
        return sri(root->left,root->right);
    }
};